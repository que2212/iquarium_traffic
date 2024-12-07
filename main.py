# import os
# import logging
# from modeling.formation import TrainFormation
# from modeling.augmentation import TrafficAugmentor
# from modeling.time_series import TrafficJamsPredictor
# from config import TestConfig, AugConfig, SeriesConfig
#
# # Настройка логирования
# logging.basicConfig(filename='traffic_model.log', level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(message)s')
#
# def run_train_formation():
#     config = TestConfig()
#     predictor = TrainFormation(directory=config.input_dir)
#     if os.path.exists(config.model_path):
#         logging.info("Модель TrainFormation найдена, используем её.")
#     else:
#         logging.info("Модель TrainFormation не найдена, запускаем обучение.")
#         predictor.date_forming()
#
# def run_traffic_augmentor():
#     config = AugConfig()
#     augmentor = TrafficAugmentor(config)
#     logging.info("Запуск TrafficAugmentor.")
#     augmentor.process_and_save()
#
# def run_traffic_jams_predictor():
#     config = SeriesConfig()
#     predictor = TrafficJamsPredictor(config)
#     if os.path.exists(config.model_path):
#         logging.info("Модель TrafficJamsPredictor найдена, используем её.")
#     else:
#         logging.info("Модель TrafficJamsPredictor не найдена, запускаем обучение.")
#         predictor.jams_catboost()
#
# if __name__ == "__main__":
#     run_train_formation()
#     run_traffic_augmentor()
#     run_traffic_jams_predictor()
#     logging.info("Все скрипты выполнены.")


# переделать