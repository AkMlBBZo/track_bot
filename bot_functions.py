import functions
import keyboard_fabric
import settings


async def start_function(bot, user_id):
    await functions.delete_keyboard(bot=bot, chat_id=user_id)
    text = settings.TEXTS.START_MESSAGE
    keyboard = keyboard_fabric.start_keyboard()
    message_id = await functions.send_message(
        bot=bot,
        chat_id=user_id,
        text=text,
        reply_markup=keyboard,
    )
    if not(settings.Bot_DB.user_exist(user_id=user_id)):
        settings.Bot_DB.add_user(user_id=user_id)
    settings.Bot_DB.set_message_id(message_id=message_id, user_id=user_id)
    return