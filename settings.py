import os
from pathlib import Path

from database_handler import BotDatabaseHandler


BASE_DIR = Path(__file__).resolve().parent

EXCEPTION_LOG = os.path.join(BASE_DIR, "exception.log")

Bot_DB = BotDatabaseHandler("data.db")

BOT_TOKEN = "6339387408:AAH-zrIxVltKRO2tyDkIbVOCf72H6wAlvog"

class TEXTS:
    START_MESSAGE = "Привет! Это бот - аудиогид по Ставрополю\n\nТебе необходимо выбрать экскурсию. Дальнейшее руководство получишь после выбора.\n(Все бесплатно)"
    BEFORE_WAY_MESSAGE = "Отлично, теперь перейди в данное место, можешь ориентироваться на фотографию"


class ACTIONS:
    SELECT_WAY = "SELECT_WAY"
    START_WAY = "START_WAY"
    MAIN_MENU = "MAIN_MENU"


class BUTTON_TEXTS:
    START_WAY = "Начать экскурсию"
    MAIN_MENU = "В меню"