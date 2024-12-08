import warnings
from fastapi import FastAPI
from threading import Thread
from parsing.scheduler import ParserScheduler
from modeling.run_modeling import TrafficPipeline


# Инициализация FastAPI
app = FastAPI()
warnings.filterwarnings("ignore", category=DeprecationWarning)


# Запуск планировщика
def start_scheduler():
    scheduler = ParserScheduler()
    scheduler.setup_schedule()
    scheduler.start()


# Запуск моделей
def run_models():
    pipeline = TrafficPipeline()
    pipeline.run_formation()
    pipeline.run_augmentation()
    pipeline.run_ts_pred()


# on_event для старта
@app.on_event("startup")
async def startup():
    scheduler_thread = Thread(target=start_scheduler, daemon=True)
    models_thread = Thread(target=run_models, daemon=True)

    scheduler_thread.start()
    models_thread.start()


# Корневой эндпоинт
@app.get("/")
def read_root():
    return {"message": "Система запущена. Планировщик и модели работают."}


# Git Bash  - консоль
# #!/bin/bash
# start "" bash -c "uvicorn main:app --log-level debug; exec bash"
# start "" bash -c "curl http://127.0.0.1:8000/; exec bash"
