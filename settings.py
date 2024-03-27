import os
from pathlib import Path

from database_handler import BotDatabaseHandler


BASE_DIR = Path(__file__).resolve().parent

EXCEPTION_LOG = os.path.join(BASE_DIR, "exception.log")

Bot_DB = BotDatabaseHandler("data.db")

# BOT_TOKEN = "6339387408:AAH-zrIxVltKRO2tyDkIbVOCf72H6wAlvog"
BOT_TOKEN = "6591690689:AAFowjUboW1ZvmfiQNBhDDE6jQVTIzVhBqw"

cities_dict = {
    -1: "Не указан",
    0: "Ставрополь"
}

class TEXTS:
    START_MESSAGE = "<b>Здравствуй 😉!</b>\nЯ - аудиогид по Ставрополю\n\nТебе необходимо выбрать экскурсию. Дальнейшее руководство получишь после выбора.\n(Все бесплатно)"
    BEFORE_WAY_MESSAGE = "Отлично, теперь пройди в данное место 🗺\nОбъект, о котором мы поговорим далее, изображен на фотографии."


class ACTIONS:
    SELECT_WAY = "SELECT_WAY"
    START_WAY = "START_WAY"
    MAIN_MENU = "MAIN_MENU"
    CONFIRM_LOCATION = "CONFIRM_LOCATION"
    CONFIRM_LISTENED = "CONFIRM_LISTENED"

class BUTTON_TEXTS:
    START_WAY = "Начать экскурсию"
    MAIN_MENU = "В меню"
    CONFIRM_LOCATION = "На месте ✅"
    CONFIRM_LISTENED = "Прослушано ✅"