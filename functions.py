import settings
from aiogram.utils import exceptions


def EXCEPTION_WRITE(exception):
    with open(settings.EXCEPTION_LOG, 'a') as file:
        file.write(str(exception) + '\n'*3)
    return


async def delete_keyboard(bot, chat_id):
    message_id = settings.Bot_DB.get_message_id(user_id=chat_id)
    try:
        await bot.edit_message_reply_markup(
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=None
        )
    except exceptions.MessageToEditNotFound:
        pass
    except Exception as e:
        EXCEPTION_WRITE(e)
    return


async def edit_message(bot, chat_id, message_id, text, reply_markup = None, parse_mode = "HTML"):
    try:
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )
    except exceptions.MessageNotModified:
        pass
    except exceptions.MessageCantBeEdited:
        try:
            await bot.delete_message(
                chat_id=chat_id,
                message_id=message_id
            )
        except exceptions.MessageToDeleteNotFound:
            pass
        msg = await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )
        settings.Bot_DB.set_message_id(msg.message_id, chat_id)
    except Exception as e:
        EXCEPTION_WRITE(e)
    return


async def delete_message(bot, chat_id, message_id):
    try:
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )
    except exceptions.MessageToDeleteNotFound:
        pass
    except Exception as e:
        EXCEPTION_WRITE(e)
    return


async def send_message(bot, chat_id, text, reply_markup = None, parse_mode = "HTML"):
    try:
        msg = await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )
        msg_id = msg.message_id
    except Exception as e:
        EXCEPTION_WRITE(e)
        msg_id = 0
    return msg_id


async def send_photo(bot, chat_id, image_url, reply_markup = None, caption = None, parse_mode = "HTML"):
    try:
        msg = await bot.send_photo(
            chat_id=chat_id,
            photo=image_url,
            caption=caption,
            parse_mode=parse_mode,
            reply_markup=reply_markup
        )
        msg_id = msg.message_id
    except Exception as e:
        EXCEPTION_WRITE(e)
        msg_id = 0
    return msg_id


async def send_location(bot, chat_id, coord, reply_markup = None):
    try:
        msg = await bot.send_location(
            chat_id=chat_id,
            latitude=coord[0],
            longitude=coord[1],
            reply_markup=reply_markup
        )
        msg_id = msg.message_id
    except Exception as e:
        EXCEPTION_WRITE(e)
        msg_id = 0
    return msg_id
