import os
import time
import pandas as pd
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.options import Options


class WeatherParser:
    """ПАРСИНГ ПОГОДЫ ACCUWEATHER"""

    def __init__(self, base_url, output_dir, ml_file, site_file):
        self.base_url = base_url
        self.output_dir = output_dir
        self.ml_file = os.path.join(output_dir, ml_file)
        self.site_file = os.path.join(output_dir, site_file)
        os.makedirs(self.output_dir, exist_ok=True)

    # Инициализация драйвера
    def create_headless_driver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        return webdriver.Chrome(options=options)

    # Прокрутка страницы и масштабирование
    def scroll_and_zoom(self, driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        driver.execute_script("document.body.style.zoom='10%'")
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    # Дф для сайта
    def process_site_data(self, df):
        df["time"] = df["time"].apply(lambda x: f"{int(x):02d}:00")
        df["weekday"] = (
            pd.to_datetime(df["date"], format="%d.%m.%Y")
            .dt.strftime("%A")
            .map(
                {
                    "Monday": "Понедельник",
                    "Tuesday": "Вторник",
                    "Wednesday": "Среда",
                    "Thursday": "Четверг",
                    "Friday": "Пятница",
                    "Saturday": "Суббота",
                    "Sunday": "Воскресенье",
                }
            )
        )
        return df

    # Дф для модели
    def process_ml_data(self, df):
        df["time"] = df["time"].apply(
            lambda x: f"{int(x):02d}:00" if ":" not in x else x.strip()
        )
        df["date"] = pd.to_datetime(
            df["date"] + " " + df["time"], format="%d.%m.%Y %H:%M"
        )
        df = df.drop(columns=["time"])
        df["temp"] = df["temp"].str.replace(r"[^\d\-]", "", regex=True).astype("int8")
        df["weather"] = df["weather"].str.lower()
        df["weather"] = df["weather"].apply(
            lambda x: (
                "clear"
                if "ясн" in x or "солн" in x
                else (
                    "cloudy"
                    if "облач" in x
                    else (
                        "rain"
                        if "дожд" in x or "ливен" in x
                        else "fog" if "тум" in x else "другое"
                    )
                )
            )
        )
        df["weather"] = df["weather"].astype("category")

        df["hour"] = df["date"].dt.hour.astype("category")
        df["hour_type"] = (
            df["hour"]
            .apply(
                lambda x: (
                    "morning"
                    if 6 <= x < 12
                    else (
                        "afternoon"
                        if 12 <= x < 18
                        else "evening" if 18 <= x < 24 else "night"
                    )
                )
            )
            .astype("category")
        )
        df["weekday"] = df["date"].dt.strftime("%A").str.lower().astype("category")
        df["day_type"] = (
            df["weekday"]
            .apply(lambda x: ("holiday" if x in ["saturday", "sunday"] else "workday"))
            .astype("category")
        )

        return df

    # Парсим данные
    def fetch_data_for_day(self, day, today):
        date = (today + timedelta(days=day)).strftime("%d.%m.%Y")
        driver = self.create_headless_driver()
        try:
            url = f"{self.base_url}?day={day + 1}"
            driver.get(url)
            self.scroll_and_zoom(driver)
            weather_data = []
            hour_blocks = driver.find_elements(
                By.CSS_SELECTOR, "div.accordion-item.hour"
            )
            for block in hour_blocks:
                time_elem = block.find_element(By.CSS_SELECTOR, "h2.date div").text
                temp_elem = block.find_element(By.CSS_SELECTOR, "div.temp.metric").text
                weather_elem = block.find_element(By.CSS_SELECTOR, "div.phrase").text
                weather_data.append((date, time_elem, temp_elem, weather_elem))
            df = pd.DataFrame(weather_data, columns=["date", "time", "temp", "weather"])
            return df
        finally:
            driver.quit()

    # Обновление дф
    def update_data(self, existing_df, new_df):
        existing_dates = pd.to_datetime(existing_df["date"])
        new_df = new_df[~pd.to_datetime(new_df["date"]).isin(existing_dates)]
        return pd.concat([existing_df, new_df], ignore_index=True)

    # Основная функция
    def weather_parsing(self):
        today = datetime.now()
        days_to_update = range(3)
        weather_data = []

        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [
                executor.submit(self.fetch_data_for_day, day, today)
                for day in days_to_update
            ]
            for future in futures:
                weather_data.append(future.result())

        raw_df = pd.concat(weather_data, ignore_index=True)
        site_df = self.process_site_data(raw_df)
        ml_df = self.process_ml_data(raw_df)

        if os.path.exists(self.ml_file):
            existing_ml_df = pd.read_csv(self.ml_file, encoding="utf-8")
            ml_df = self.update_data(existing_ml_df, ml_df)
        ml_df.to_csv(self.ml_file, index=False, encoding="utf-8")

        if os.path.exists(self.site_file):
            existing_site_df = pd.read_csv(self.site_file, encoding="utf-8")
            site_df = self.update_data(existing_site_df, site_df)
        site_df.to_csv(self.site_file, index=False, encoding="utf-8")
