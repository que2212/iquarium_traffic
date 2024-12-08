import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class ScoreParser:
    """ПАРСИНГ БАЛЬНОСТИ YAMAPS"""

    def __init__(self, base_url, output_dir, site_file):
        self.base_url = base_url
        self.output_dir = output_dir
        self.site_file = os.path.join(output_dir, site_file)
        os.makedirs(self.output_dir, exist_ok=True)

    # Инициализация драйвера
    def create_headless_driver(self):
        options = Options()
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        return webdriver.Chrome(options=options)

    # Парсинг данных
    def fetch_traffic_score(self):
        driver = self.create_headless_driver()
        try:
            driver.get(self.base_url)
            traffic_score_elem = driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[2]/div[11]/div/div[1]/div[1]/div[1]"
                "/div/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]"
            )
            traffic_score = traffic_score_elem.text.strip()
            df = pd.DataFrame({"score": [traffic_score]})
            return df
        finally:
            driver.quit()

    # Сохранение
    def save_data(self, df):
        df.to_csv(self.site_file, index=False, encoding="utf-8")

    # Основная функция
    def parse_traffic(self):
        df = self.fetch_traffic_score()
        self.save_data(df)
