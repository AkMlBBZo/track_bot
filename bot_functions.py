import functions
import keyboards
from main import storage
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
    
    keyboard = keyboard_fabric.confirm_way_keyboard(user_id)
    text = settings.TEXTS.BEFORE_WAY_MESSAGE
    image_path = settings.Bot_DB.get_start_photo_path(way_id=way_id)
    coord = settings.Bot_DB.get_start_coord(way_id=way_id)
    coords = settings.Bot_DB.get_coords(way_id=way_id)

    await functions.send_location(
        bot=bot,
        chat_id=user_id,
        coord=coord
    )

    message_id = await functions.send_photo(
        bot=bot,
        chat_id=user_id,
        caption=text,
        image_url=image_path,
        reply_markup=keyboard
    )

    settings.Bot_DB.set_select_route(select_route=way_id, user_id=user_id)
    settings.Bot_DB.set_message_id(message_id=message_id, user_id=user_id)
    return

async def confirm_way_function(bot, user_id):
    # Deleted keyboard
    await functions.delete_keyboard(bot=bot, chat_id=user_id)

    # Get data from DB
    way_id = settings.Bot_DB.get_select_route(user_id=user_id)
    coords = settings.Bot_DB.get_coords(way_id=way_id)
    audio_path = settings.Bot_DB.get_audio_paths(way_id=way_id)
    image_url = settings.Bot_DB.get_photo_path(way_id=way_id)
    texts = settings.Bot_DB.get_texts(way_id=way_id)

    # We get the num of points in the way
    num_of_steps = len(texts)

    try:
        data = await storage.get_data(chat=user_id, user=user_id)
        data['step']
    except:
        await storage.set_data(chat=user_id, user=user_id, data={"step": 0})
        data = await storage.get_data(chat=user_id, user=user_id)

    step = data['step']

    if step < num_of_steps:

        # Keyboard generated 
        keyboard_audio = keyboard_fabric.confirm_listened_keyboard(user_id)

        if step > 0:
            await functions.send_location(
                bot=bot,
                chat_id=user_id,
                coord=coords[step],
                )

        if image_url != None:
            await functions.send_photo(
                bot=bot,
                chat_id=user_id,
                image_url=image_url[step],
                caption=texts[step],
            )
        
        else:
            await functions.send_message(
                bot=bot,
                chat_id=user_id,
                text="<i>У этого объекта нет фотографии.</i>",
            )

        if audio_path:
            audio = open(audio_path[step], "rb").read()
            message = await functions.send_message(
                bot=bot,
                chat_id=user_id,
                text="<i>Отправляю аудио файл...</i>",
                parse_mode='HTML'
            )

            message_id = await functions.send_audio(
                bot=bot,
                chat_id=user_id,
                audio=audio,
                reply_markup=keyboard_audio,
            )

            await functions.delete_message(
                bot=bot,
                chat_id=user_id,
                message_id=message
            )

        else:
            message_id = await functions.send_message(
                bot=bot,
                chat_id=user_id,
                text="<i>У этого объекта нет аудиофайла.</i>",
            )
        await storage.update_data(chat=user_id, user=user_id, data={"step": step+1})


    else:
        keyboard = keyboard_fabric.universal_keyboard(keyboard=keyboards.END_KEYBOARD)
        message_id = await functions.send_message(
            bot=bot, 
            chat_id=user_id, 
            text="Вы закончили данный маршрут!",
            reply_markup=keyboard
        )
        await storage.update_data(chat=user_id, user=user_id, data={})

    
    if not(settings.Bot_DB.user_exist(user_id=user_id)):
        settings.Bot_DB.add_user(user_id=user_id)
    settings.Bot_DB.set_message_id(message_id=message_id, user_id=user_id)
    return