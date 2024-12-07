import os
import pandas as pd
from config import TestConfig
from janitor import clean_names


class TrainFormation:
    """СБОРКА TRAIN/TEST ДЛЯ TENSORFLOW"""

    def __init__(self, directory="data"):
        self.directory = directory
        self.data_dict = {}
        self.na_counts = {}

    # Импорт
    def import_csv(self):
        files = [
            os.path.join(self.directory, file)
            for file in os.listdir(self.directory)
            if file.endswith(".csv")
        ]

        for file in files:
            df = clean_names(pd.read_csv(file, na_values=["N/A", "NA", "", "."]))
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"])
            data_name = os.path.splitext(os.path.basename(file))[0]
            self.data_dict[data_name] = df
            self.na_counts[data_name] = df.isna().sum().sum()

        na_df = pd.DataFrame(
            list(self.na_counts.items()), columns=["dataset", "na_count"]
        )
        return self.data_dict, na_df

    # Формирование test
    def combine_dfs(self):
        ordered_keys = ["date", "weather", "traffic", "crash"]
        dfs = [self.data_dict[key] for key in ordered_keys if key in self.data_dict]
        combined_df = pd.concat(dfs, axis=1)
        if "hour" in combined_df.columns:
            combined_df = combined_df.drop(columns=["hour"])
        if "date" in combined_df.columns:
            combined_df.insert(1, "hour", combined_df["date"].dt.hour)
        return combined_df, print("train-test сформировано")

    # Сохранение
    def save_df(self, df, filename):
        df.to_excel(filename, index=False)

    # Основная функция
    def date_forming(self):
        data_dict, na_df = self.import_csv()
        combined_df = self.combine_dfs()
        return combined_df, na_df


# Использование
if __name__ == "__main__":
    config = TestConfig()
    predictor = TrainFormation(directory=config.input_dir)
    predictor.date_forming()
