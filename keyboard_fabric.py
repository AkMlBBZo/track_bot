from aiogram import types

import settings
import keyboards
import functions


def start_keyboard():
    buttons = list()
    ways = settings.Bot_DB.get_way_names()
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


def confirm_way_keyboard(user_id):
    buttons = list()
    way = settings.Bot_DB.get_select_route(user_id)
    buttons.append(
        types.InlineKeyboardButton(
            text = settings.BUTTON_TEXTS.CONFIRM_LOCATION,
            callback_data = f'{settings.ACTIONS.CONFIRM_LOCATION}{way}'
        )
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard

def confirm_listened_keyboard(user_id):
    buttons = list()
    way = settings.Bot_DB.get_select_route(user_id)
    buttons.append(
        types.InlineKeyboardButton(
            text = settings.BUTTON_TEXTS.CONFIRM_LISTENED,
            callback_data = f'{settings.ACTIONS.CONFIRM_LOCATION}{way}'
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