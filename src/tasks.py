from bot import app, bot, TELEGRAM_CHANNEL_ID
import logging
from aiogram.types import InputFile
import asyncio

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.task(rate_limit='1/d',)
def send_audio_and_message_to_telegram(audio_path, message_text):
    logger.info("Starting audio and message transmission to Telegram.")

    # Отправка аудио и сообщения в Telegram
    loop = asyncio.get_event_loop()
    loop.run_until_complete(transmit_audio_and_message(audio_path, message_text))


async def transmit_audio_and_message(audio_path, message_text):
    # Отправка аудиофайла
    await bot.send_audio(TELEGRAM_CHANNEL_ID, InputFile(audio_path))
    logger.info(f"Audio file {audio_path} sent to Telegram.")

    # Отправка текстового сообщения
    await bot.send_message(TELEGRAM_CHANNEL_ID, message_text)
    logger.info(f"Message '{message_text}' sent to Telegram.")
