import settings
from aiogram.utils import exceptions


async def delete_keyboard(bot, chat_id):
    message_id = settings.Bot_DB.get_message_id(user_id=chat_id)
    try:
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
    except:
        pass
    return


async def edit_message(bot, chat_id, message_id, text, reply_markup = None, parse_mode = "HTML"):
    try:
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=reply_markup, parse_mode=parse_mode)
    except exceptions.MessageNotModified:
        pass
    except exceptions.MessageCantBeEdited:
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except exceptions.MessageToDeleteNotFound:
            pass
        msg = await bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode=parse_mode)
        settings.Bot_DB.set_message_id(msg.message_id, chat_id)
    return


async def delete_message(bot, chat_id, message_id):
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except exceptions.MessageToDeleteNotFound:
        pass
    return


async def send_message(bot, chat_id, text, reply_markup = None, parse_mode = "HTML"):
    try:
        msg = await bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode=parse_mode)
        msg_id = msg.message_id
    except:
        msg_id = 0
    return msg_id