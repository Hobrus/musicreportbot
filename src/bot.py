import logging
import os

from aiogram import Bot, Dispatcher
from celery import Celery
from dotenv import load_dotenv

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузите переменные среды
load_dotenv()
logger.info("Environment variables loaded.")

# Параметры из .env.example
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
GRAFANA_URL = os.getenv("GRAFANA_URL")

# Настройка aiogram
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
logger.info("Aiogram setup complete.")

# Настройка Celery
app = Celery('bot', broker='redis://redis:6379/0')
logger.info("Celery setup complete.")


if __name__ == "__main__":
    logger.info("Starting the bot.")
    from aiogram import executor

    executor.start_polling(dp)
    logger.info("Bot stopped.")
