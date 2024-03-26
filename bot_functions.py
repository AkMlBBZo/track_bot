import functions
import keyboards
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

async def select_way_function(bot, user_id, action):
    await functions.delete_keyboard(bot=bot, chat_id=user_id)
    
    way_id = int( action.replace( settings.ACTIONS.SELECT_WAY, "" ) )
    
    keyboard = keyboard_fabric.universal_keyboard(keyboards.START_WAY_KEYBOARD)
    text = settings.TEXTS.BEFORE_WAY_MESSAGE
    image_path = settings.Bot_DB.get_start_photo_path(way_id=way_id)
    coord = settings.Bot_DB.get_start_coord(way_id=way_id)

    await functions.send_photo(
        bot=bot,
        chat_id=user_id,
        image_url=image_path
    )
    await functions.send_location(
        bot=bot,
        chat_id=user_id,
        coord=coord
    )
    message_id = await functions.send_message(
        bot=bot,
        chat_id=user_id,
        text=text,
        reply_markup=keyboard
    )

    settings.Bot_DB.set_message_id(message_id=message_id, user_id=user_id)
    settings.Bot_DB.set_select_route(select_route=way_id, user_id=user_id)
    return
