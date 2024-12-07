import os
import numpy as np
import pandas as pd
import concurrent.futures
from config import AugConfig
from janitor import clean_names
from tensorflow.keras import Sequential
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM, Dense, Dropout


class TrafficAugmentor:
    """TENSORFLOW MODEL"""

    def __init__(self, config):
        self.input_dir = os.path.dirname(config.train_csv)
        self.models_dir = config.models_dir
        self.weather_file = config.pre_train

    # Импорт данных
    def import_csv(self):
        files = [
            os.path.join(self.input_dir, file)
            for file in os.listdir(self.input_dir)
            if file.endswith(".csv")
        ]
        data_dict = {}
        na_counts = {}

        for file in files:
            df = clean_names(pd.read_csv(file, na_values=["N/A", "NA", "", "."]))
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"])
            data_name = os.path.splitext(os.path.basename(file))[0]
            data_dict[data_name] = df
            na_counts[data_name] = df.isna().sum().sum()

        na_df = pd.DataFrame(list(na_counts.items()), columns=["dataset", "na_count"])
        return data_dict, na_df

    # Целевая переменная traffic
    def aug_traffic(self, weather_data, train_data):
        scaler = MinMaxScaler()
        scaled_train_traffic = scaler.fit_transform(
            train_data["traffic"].values.reshape(-1, 1)
        )
        scaled_weather = scaler.fit_transform(weather_data)

        X, y = [], []
        for i in range(len(scaled_train_traffic) - 1):
            X.append(scaled_train_traffic[i : i + 1])
            y.append(scaled_train_traffic[i + 1])
        X, y = np.array(X), np.array(y)

        model = Sequential(
            [
                LSTM(100, activation="relu", return_sequences=True, input_shape=(1, 1)),
                Dropout(0.2),
                LSTM(50, activation="relu"),
                Dense(1),
            ]
        )
        model.compile(optimizer="adam", loss="mse")
        model.fit(X, y, epochs=100, batch_size=16, verbose=0)

        self.save_model(model)

        synthetic_traffic = []
        current_input = scaled_weather[:1]
        for _ in range(len(weather_data)):
            pred = model.predict(current_input.reshape(1, 1, -1), verbose=0)
            synthetic_traffic.append(pred[0][0])
            current_input = (
                np.vstack([current_input[0][1:], pred])
                if current_input.shape[1] > 1
                else pred
            )

        synthetic_traffic = scaler.inverse_transform(
            np.array(synthetic_traffic).reshape(-1, 1)
        )
        return synthetic_traffic.flatten()

    @staticmethod
    # Аварии
    def aug_crash(length, train_crashes):
        crash_prob = train_crashes.mean() / train_crashes.max()
        return np.random.binomial(1, crash_prob, size=length) * np.random.randint(
            1, train_crashes.max() + 1, size=length
        )

    @staticmethod
    # Адреса
    def aug_addresses(train_df, crashes):
        addresses = train_df["address"].unique()
        return [np.random.choice(addresses) if crash != 0 else 0 for crash in crashes]

    # Собираем дф
    def all_test_data(self, weather_ml_df, train_df):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            traffic_future = executor.submit(
                self.aug_traffic, weather_ml_df[["temp"]].values, train_df
            )
            crash_future = executor.submit(
                self.aug_crash, len(weather_ml_df), train_df["crash"].values
            )
            synthetic_traffic = traffic_future.result()
            synthetic_crash = crash_future.result()
            synthetic_addresses = self.aug_addresses(train_df, synthetic_crash)

        weather_ml_df["traffic"] = synthetic_traffic
        weather_ml_df["crash"] = synthetic_crash
        weather_ml_df["address"] = synthetic_addresses

        return weather_ml_df

    # Экспорт модели
    def save_model(self, model):
        model_path = os.path.join(self.models_dir, "traffic_lstm.h5")
        model.save(model_path)

    # Экспорт тестовых данных
    def save_csv(self, data_frame, path):
        data_frame.to_csv(path, index=False)

    # Основная функция
    def process_and_save(self):
        data_dict, _ = self.import_csv()
        train_df = data_dict["train"]
        weather_ml_df = pd.read_csv(self.weather_file)
        augmented_test_df = self.all_test_data(weather_ml_df, train_df)


# Использование
if __name__ == "__main__":
    config = AugConfig()
    augmentor = TrafficAugmentor(config)
    augmentor.process_and_save()
