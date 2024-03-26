from aiogram import types

import settings
import keyboards
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


def universal_keyboard(keyboard, row_width=1):
    buttons = list()
    for button in keyboard:
        buttons.append(
            types.InlineKeyboardButton(
                text = button[0],
                callback_data = button[1]
            )
        )
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    keyboard.add(*buttons)
    return keyboard
                
            