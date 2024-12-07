import time
import schedule
from config import ParsingConfig
from parsing.crash import CrashRoads
from parsing.score import ScoreParser
from parsing.weather import WeatherParser


class ParserScheduler:
    """ПЛАНИРОВЩИК"""

    def __init__(self):
        self.schedule = schedule
        self.config = ParsingConfig()

    # Декоратор для логирования
    @staticmethod
    def log_execution(message):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"{message}...")
                result = func(*args, **kwargs)
                return result

            return wrapper

        return decorator

    # Запуск парсинга
    @log_execution("Собираем данные о погоде...")
    def run_weather_parsing(self):
        parser = WeatherParser(
            self.config.weather_url,
            self.config.output_dir,
            self.config.weather_ml,
            self.config.weather_site,
        )
        parser.weather_parsing()
        print("Результа WeatherParser сохранён.")

    @log_execution("Собираем данные о пробках...")
    def run_score_parsing(self):
        score_parser = ScoreParser(
            self.config.score_url, self.config.output_dir, self.config.score_site
        )
        score_parser.parse_score_data()
        print("Результат ScoreParser сохранёны.")

    @log_execution("Собираем данные о ДТП...")
    def run_crashroads_parsing(self):
        crash_parser = CrashRoads(
            self.config.crash_map, self.config.crash_ml, self.config.output_dir
        )
        crash_parser.parse_crash_data()
        print("Результат CrashRoads сохранён.")

    # Настройка задач
    def setup_schedule(self):
        coded_time = (6, 0)
        time_str = f"{coded_time[0]:02d}:{coded_time[1]:02d}"

        tasks = [
            self.run_weather_parsing,
            self.run_score_parsing,
            self.run_crashroads_parsing,
        ]

        for task in tasks:
            self.schedule.every().day.at(time_str).do(task)

    # Запуск цикла
    def start(self):
        print("Запуск планировщика...")
        print("Данные уже обновлены.")
        print("Следующий сбор данных в 06:00.")
        while True:
            self.schedule.run_pending()
            time.sleep(1)


# Использование
if __name__ == "__main__":
    scheduler = ParserScheduler()
    scheduler.setup_schedule()
    scheduler.start()
