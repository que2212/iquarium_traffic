import os
import json
import optuna
import numpy as np
import pandas as pd
from janitor import clean_names
from config import SeriesConfig
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, RobustScaler


class TrafficJamsPredictor:
    """CATBOOST WITH FOURIER SERIES MODEL"""

    def __init__(self, config):
        self.config = config
        self.data_dict, self.na_info = self.create_dict()
        self.processed_df, self.scaler = self.encoding_vars()
        self.to_category = []

    # Словарь с дф
    def create_dict(self):
        files = [
            os.path.join(self.config.data_dir, file)
            for file in os.listdir(self.config.data_dir)
            if file.endswith(".csv")
        ]
        data_dict = {}
        na_counts = {}

        for file in files:
            df = clean_names(pd.read_csv(file, na_values=["N/A", "NA", "", "."]))

            data_type = "train" if "train" in file.lower() else "test"
            df["data_type"] = data_type

            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"])

            data_name = os.path.splitext(os.path.basename(file))[0]
            data_dict[data_name] = df
            na_counts[data_name] = df.isna().sum().sum()

        na_df = pd.DataFrame(list(na_counts.items()), columns=["dataset", "na_count"])
        return data_dict, na_df

    # Кодирование переменных
    def encoding_vars(self):
        combined_df = pd.concat(self.data_dict.values(), ignore_index=True)

        combined_df = combined_df.sort_values(
            by=["data_type", "date"], ascending=[True, True]
        )
        combined_df.reset_index(drop=True, inplace=True)

        if "jams" in combined_df.columns:
            combined_df["jams"] = combined_df["jams"].astype("float64")

        to_int8 = ["temp", "crash", "traffic"]
        for col in to_int8:
            if col in combined_df.columns:
                combined_df[col] = combined_df[col].astype("int8", errors="ignore")

        label_encoder = LabelEncoder()
        to_encode = ["weekday", "day_type", "hour_type", "weather", "address"]
        for col in to_encode:
            if col in combined_df.columns:
                combined_df[col] = label_encoder.fit_transform(
                    combined_df[col].astype(str)
                )

        numerical_cols = ["temp", "traffic", "crash", "jams"]
        scaler = RobustScaler()
        combined_df[numerical_cols] = scaler.fit_transform(combined_df[numerical_cols])

        priority = {"train": 0, "test": 1}
        combined_df = combined_df.sort_values(
            by=["data_type", "date"],
            key=lambda col: col.map(priority) if col.name == "data_type" else col,
            ascending=[True, True],
        )

        return combined_df, scaler

    # Ряды Фурье
    def fourier_features(self, df, hour_col="hour", max_frequency=4):
        df = df.copy()
        for freq in range(1, max_frequency + 1):
            df[f"sin_{freq}"] = np.sin(2 * np.pi * freq * df[hour_col] / 24)
            df[f"cos_{freq}"] = np.cos(2 * np.pi * freq * df[hour_col] / 24)

        return df

    # Подготовка датасетов
    def prepare_for_modeling(
        self, df, target_col="jams", test_size=0.3, random_state=42
    ):
        train_data = df[df["data_type"] == "train"].drop(columns=["address", "date"])
        test_data = df[df["data_type"] == "test"].drop(
            columns=["address", "date", target_col, "data_type"]
        )

        X = train_data.drop(columns=[target_col, "data_type"])
        y = train_data[target_col]

        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        return X_train, X_val, y_train, y_val, test_data

    # Гиперпараметры
    def objective(self, trial):
        param = {
            "iterations": trial.suggest_int("iterations", 500, 2500),
            "learning_rate": trial.suggest_float("learning_rate", 1e-3, 0.1, log=True),
            "depth": trial.suggest_int("depth", 2, 6),
            "l2_leaf_reg": trial.suggest_float("l2_leaf_reg", 1e-2, 10.0),
            "bagging_temperature": trial.suggest_float("bagging_temperature", 0.0, 1.0),
            "random_strength": trial.suggest_float("random_strength", 0.0, 1.0),
            "border_count": trial.suggest_int("border_count", 1, 255),
        }

        model = CatBoostRegressor(
            **param,
            early_stopping_rounds=50,
            eval_metric="RMSE",
            task_type="GPU",
            cat_features=self.to_category,
            verbose=2,
        )
        model.fit(
            self.X_train, self.y_train, eval_set=(self.X_val, self.y_val), verbose=2
        )

        preds = model.predict(self.X_val)
        mse = mean_squared_error(self.y_val, preds)
        rmse = np.sqrt(mse)
        return mse, rmse

    # Optuna для тюнинга
    def run_optuna(self):
        study = optuna.create_study(
            sampler=optuna.samplers.CmaEsSampler(), direction="minimize"
        )
        study.optimize(self.objective, n_trials=50, show_progress_bar=True)
        best_params = study.best_params
        with open(self.config.best_params_file, "w") as file:
            json.dump(best_params, file)
        return best_params

    # Проверка параметорв
    def load_best_params(self):
        if os.path.exists(self.config.best_params_file):
            with open(self.config.best_params_file, "r") as file:
                best_params = json.load(file)
        else:
            best_params = self.run_optuna()
        return best_params

    # Промерка модели
    def check_and_load_model(self):
        if os.path.exists(self.config.model_file):
            model = CatBoostRegressor()
            model.load_model(self.config.model_file)
            return model
        else:
            return None

    # Обучение
    def train_model(self, X_train, y_train, X_val, y_val, cat_features):
        os.environ["CATBOOST_INFO_DIR"] = os.path.normpath(self.config.catboost_info_dir)
        model = self.check_and_load_model()
        if model is None:
            best_params = self.load_best_params()
            model = CatBoostRegressor(
                **best_params,
                cat_features=cat_features,
                eval_metric="RMSE",
                task_type="GPU",
                verbose=2,
            )
            model.fit(X_train, y_train, eval_set=[(X_val, y_val)])
            self.save_model(model)
        return model

    # Сдвиг
    def add_shift(self, predictions, noise_level=1):
        shift = np.random.uniform(noise_level, size=predictions.shape)
        return predictions + shift

    # Экспорт модели
    def save_model(self, model, filename=None):
        if filename is None:
            filename = self.config.model_file
        model.save_model(filename)

    # Экспорт результатов
    def save_results(self, predictions, filename=None):
        if filename is None:
            filename = self.config.jams_pred
        predictions.to_csv(filename, index=False, encoding="utf-8")

    # Основная функция
    def jams_catboost(self):
        processed_df = self.fourier_features(self.processed_df.copy())

        test_data_original = self.processed_df[
            self.processed_df["data_type"] == "test"
        ].copy()
        test_data = test_data_original.drop(
            columns=["address", "date", "jams", "data_type"]
        )

        X_train, X_val, y_train, y_val, test_data = self.prepare_for_modeling(
            processed_df
        )
        self.X_train, self.X_val, self.y_train, self.y_val = (
            X_train,
            X_val,
            y_train,
            y_val,
        )
        best_model = self.train_model(X_train, y_train, X_val, y_val, self.to_category)

        y_pred = best_model.predict(X_val)
        mse = mean_squared_error(y_val, y_pred)
        rmse = np.sqrt(mse)

        test_predictions = best_model.predict(test_data)

        numerical_cols = ["temp", "traffic", "crash", "jams"]
        test_predictions_rescaled = self.scaler.inverse_transform(
            np.column_stack(
                [
                    np.zeros((len(test_predictions), len(numerical_cols) - 1)),
                    test_predictions,
                ]
            )
        )[:, -1]

        test_predictions_final = self.add_shift(test_predictions_rescaled)
        test_predictions_final = np.clip(np.round(test_predictions_final), 0, 9).astype(
            int
        )

        result = pd.DataFrame(
            {
                "date": test_data_original["date"],
                "hour": test_data_original["hour"],
                "predicted_jams": test_predictions_final,
            },
            index=test_data_original.index,
        )

        self.save_model(best_model)
        self.save_results(result)


# Использование
if __name__ == "__main__":
    config = SeriesConfig()
    predictor = TrafficJamsPredictor(config)
    predictor.jams_catboost()
