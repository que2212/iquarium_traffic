import os

BASE_DIR = os.path.dirname(os.path.abspath("."))


class ParsingConfig:
    """КОНФИГУРАЦИЯ ДЛЯ ПАРСИНГА"""

    def __init__(self):
        self.weather_url = "https://www.accuweather.com/ru/ru/krasnodar/293686/hourly-weather-forecast/293686"
        self.weather_site = "weather_site.csv"
        self.weather_ml = "weather_ml.csv"

        self.score_url = "https://yandex.ru/maps/35/krasnodar/probki/"
        self.score_site = "score_site.csv"

        self.crash_map = "./data/raw/cr_map.geojson"
        self.crash_ml = "cr_map.csv"

        self.output_dir = "./data/raw"


class TestConfig:
    """КОНФИГУРАЦИЯ ДЛЯ TRAIN/TEST"""

    def __init__(self):
        self.input_dir = "./data/draft"
        self.trte_output_dir = "./data/result"
        self.test_csv = "./data/result/test.csv"


class AugConfig:
    """КОНФИГУРАЦИЯ ДЛЯ МОДЕЛИ TF"""

    def __init__(self):
        self.models_dir = "./models"
        self.test_csv = "./data/result/test.csv"
        self.train_csv = "./data/result/train.csv"
        self.pre_train = "./data/raw/weather_ml.csv"


class SeriesConfig:
    """КОНФИГУРАЦИЯ ДЛЯ МОДЕЛИ CATBOOST"""

    def __init__(self):
        self.models_dir = "./models"
        self.data_dir = "./data/result"
        self.jams_pred = "./data/result/jams_pred.csv.csv"
        self.model_file = os.path.join(self.models_dir, "jams_boost.cbm")
        self.catboost_info_dir = os.path.join(self.models_dir, "catboost_info")
        self.best_params_file = os.path.join(self.models_dir, "best_params.json")

        os.makedirs(self.models_dir, exist_ok=True)
        os.makedirs(self.catboost_info_dir, exist_ok=True)
