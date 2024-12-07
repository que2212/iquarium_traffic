import os
import re
import json
import random
import pandas as pd


class CrashRoads:
    """КАРТА АВАРИЙНОСТИ"""

    def __init__(self, geojson_path, crash_ml, output_dir):
        self.geojson_path = geojson_path
        self.output_dir = output_dir
        self.crash_file = os.path.join(output_dir, crash_ml)
        os.makedirs(self.output_dir, exist_ok=True)
        self.data = self._load_geojson()

    # Импорт из GeoJSON
    def _load_geojson(self):
        with open(self.geojson_path, encoding="utf-8") as f:
            geojson_data = json.load(f)
        return [feature["properties"] for feature in geojson_data["features"]]

    # Процессинг
    def filter_and_process_data(self):
        df = pd.DataFrame(self.data)
        df = df[df["region"] == "Краснодар"]

        df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce").dt.floor("H")
        df = df[df["datetime"].dt.year == 2024]
        df = df[df["datetime"].dt.month == 9]
        df["hour"] = df["datetime"].dt.hour

        df["weather"] = df["weather"].apply(
            lambda x: x[0] if isinstance(x, list) else x
        )

        df["address"] = df["address"].apply(self._clean_address)

        df["address"] = df.apply(
            lambda row: self.replace_na(row, df["address"]),
            axis=1,
        )

        return df

    # Новая переменная
    def group_and_aggregate_data(self, df):
        grouped_df = (
            df.groupby("datetime")
            .agg(
                {
                    "address": lambda x: ", ".join(x.unique()),
                    "hour": "first",
                    "weather": "first",
                }
            )
            .reset_index()
        )

        grouped_df["crash"] = grouped_df["address"].apply(lambda x: len(x.split(", ")))

        grouped_df = grouped_df.sort_values(by="datetime", ascending=False)
        grouped_df.reset_index(drop=True, inplace=True)
        return grouped_df

    # Стандартизация адресса
    def _clean_address(self, address):
        if isinstance(address, str):
            match = re.search(r"ул\s+([^\d,]+)", address)
            address = match.group(1).strip() if match else pd.NA
            address = (
                re.sub(r"^им\s+", "", address) if isinstance(address, str) else address
            )
            return address.replace(" ", "_") if isinstance(address, str) else address
        return pd.NA

    # Заполнение na
    def replace_na(self, row, address_column):
        if pd.isna(row["address"]):
            return random.choice(address_column.dropna().tolist())
        return row["address"]

    # Распределние
    def distribute_crashes(self, grouped_df):
        # Создаем шаблон всех дней и часов
        dates = pd.DataFrame(
            {"date": pd.date_range(start="2024-11-23", end="2024-11-30", freq="D")}
        )
        hours = pd.DataFrame({"hour": range(24)})
        template = dates.merge(hours, how="cross")
        total_crashes = grouped_df["crash"].sum()

        daily_crashes = []
        for date in template["date"].unique():
            if pd.to_datetime(date).weekday() >= 5:
                daily_count = random.randint(2, 5)
            else:
                daily_count = random.randint(4, 8)
            daily_crashes.append((date, daily_count))

        daily_crashes = pd.DataFrame(
            daily_crashes, columns=["date", "daily_crash_count"]
        )
        scale_factor = total_crashes / daily_crashes["daily_crash_count"].sum()
        daily_crashes["daily_crash_count"] = (
            (daily_crashes["daily_crash_count"] * scale_factor).round().astype(int)
        )

        template["crash"] = 0
        template["address"] = None

        for _, row in daily_crashes.iterrows():
            date = row["date"]
            daily_count = row["daily_crash_count"]
            available_hours = template[template["date"] == date]["hour"].tolist()
            random_hours = random.choices(available_hours, k=daily_count)

            for hour in set(random_hours):
                crash_count = random_hours.count(hour)
                idx = template[
                    (template["date"] == date) & (template["hour"] == hour)
                ].index[0]

                selected_addresses = random.sample(
                    grouped_df["address"].tolist(), crash_count
                )
                template.loc[idx, "crash"] = crash_count
                template.loc[idx, "address"] = ", ".join(selected_addresses)

        return template

    # Основная функция
    def crash_map(self):
        processed_df = self.filter_and_process_data()
        grouped_df = self.group_and_aggregate_data(processed_df)
        distributed_df = self.distribute_crashes(grouped_df)
        distributed_df.to_csv(self.crash_file, index=False, encoding="utf-8")
        return distributed_df
