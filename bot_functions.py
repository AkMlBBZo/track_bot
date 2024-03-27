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
        # parse_mode='HTML'
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
    print(len(coords), coords)

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

    # message_id = await functions.send_message(
    #     bot=bot,
    #     chat_id=user_id,
    #     text=text,
    #     reply_markup=keyboard
    # )

    settings.Bot_DB.set_select_route(select_route=way_id, user_id=user_id)
    settings.Bot_DB.set_message_id(message_id=message_id, user_id=user_id)
    return

async def confirm_way_function(bot, user_id, action):
    await functions.delete_keyboard(bot=bot, chat_id=user_id)
    way_id = int( action.replace( settings.ACTIONS.CONFIRM_LOCATION, "" ) )
    # keyboard_message = keyboard_fabric.confirm_way_keyboard(user_id)
    keyboard_audio = keyboard_fabric.confirm_listened_keyboard(user_id)
    audio_path = settings.Bot_DB.get_audio_paths(way_id=way_id)
    image_url = settings.Bot_DB.get_photo_path(way_id=way_id)
    text = settings.Bot_DB.get_texts(way_id=way_id)

    len_way = len(settings.Bot_DB.get_coords(way_id=way_id))
    try:
        data = await storage.get_data(chat=user_id, user=user_id)
        data['pos_coords']
        print('Good')
    except:
        await storage.set_data(chat=user_id, user=user_id, data={"pos_coords": 0})
        data = await storage.get_data(chat=user_id, user=user_id)
        print('Error')

    if data['pos_coords'] != len_way:
        if image_url != None:
            await functions.send_photo(
                bot=bot,
                chat_id=user_id,
                image_url=image_url[data['pos_coords']],
                caption=text[data['pos_coords']],
                # reply_markup=keyboard_audio,
            )
        
        else:
            await functions.send_message(
                bot=bot,
                chat_id=user_id,
                text="<i>У этого объекта нет фотографии.</i>",
            )

        if audio_path:
            audio = open(audio_path[data['pos_coords']], "rb").read()
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
        await storage.update_data(chat=user_id, user=user_id, data={"pos_coords": data['pos_coords']+1})
    else:
        message_id = await functions.send_message(
            bot=bot, 
            chat_id=user_id, 
            text="Вы закончили данный маршрут!"
        )

    
    if not(settings.Bot_DB.user_exist(user_id=user_id)):
        settings.Bot_DB.add_user(user_id=user_id)
    settings.Bot_DB.set_message_id(message_id=message_id, user_id=user_id)
    return