import os
import pandas as pd
from config import TestConfig, AugConfig, SeriesConfig
from modeling import TrainFormation, TrafficAugmentor, TrafficJamsPredictor


class TrafficPipeline:
    def __init__(self):
        self.formation_config = TestConfig()
        self.augmentation_config = AugConfig()
        self.series_config = SeriesConfig()

    def run_formation(self):
        print("\nformation.py")
        predictor = TrainFormation(directory=self.formation_config.input_dir)

        data_dict, na_df = predictor.import_csv()
        print("Данные импортированы.")
        print("Проверка завершена.")

        combined_df = predictor.combine_dfs()
        print("Train/test успешно сформированы.")
        print("\n/// /// /// /// ///")

    def run_augmentation(self):
        print("\naugmentation.py")
        augmentor = TrafficAugmentor(self.augmentation_config)

        data_dict, _ = augmentor.import_csv()
        print("Найдена целевая переменная.")
        print("Поиск зависимостей...")

        train_df = data_dict["train"]
        weather_ml_df = pd.read_csv(self.augmentation_config.pre_train)
        augmented_test_df = augmentor.all_test_data(weather_ml_df, train_df)
        print("Аугментация завершена.")

        model_path = os.path.join(
            self.augmentation_config.models_dir, "traffic_lstm.h5"
        )
        print(f"Модель tensorflow сохранена по пути: {model_path}")
        print("\n/// /// /// /// ///")

    def run_ts_pred(self):
        print("\ntime_series.py")
        predictor = TrafficJamsPredictor(self.series_config)

        model = predictor.check_and_load_model()

        if model is None:
            print("Модель не найдена. Запускаем обучение...")
            predictor.jams_catboost()
            print("Catboost обучена.")
        else:
            print("Catboost уже существует и была успешно загружена.")

        print("Прогноз сделан.")
        print("Результаты успешно сохранены.")
        print("\n/// /// /// /// ///")


# # Использование
# if __name__ == "__main__":
#     pipeline = TrafficPipeline()
#     pipeline.run_formation()
#     pipeline.run_augmentation()
#     pipeline.run_ts_pred()
