from aiogram import types

import settings
import functions


def start_keyboard():
    buttons = list()
    ways = settings.Bot_DB.get_way_names()
    print(ways)
    for way in ways:
        buttons.append(
            types.InlineKeyboardButton(
                text = way.name,
                callback_data = f"{settings.ACTIONS.SELECT_WAY}{way.id}"
            )
        )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard