import os
from pathlib import Path

from database_handler import BotDatabaseHandler


BASE_DIR = Path(__file__).resolve().parent

Bot_DB = BotDatabaseHandler("data.db")

BOT_TOKEN = "6339387408:AAH-zrIxVltKRO2tyDkIbVOCf72H6wAlvog"

class TEXTS:
    START_MESSAGE = "Привет! Это бот - аудиогид по Ставрополю\n\nТебе необходимо выбрать экскурсию. Дальнейшее руководство получишь после выбора.\n(Все бесплатно)"


class ACTIONS:
    SELECT_WAY = "SELECT_WAY"