import settings
import bot_functions

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

bot = Bot(token=settings.BOT_TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message):
    await bot_functions.start_function(bot=bot,
                                       user_id=message.from_user.id)

@dp.callback_query_handler(state="*")
async def callback_handler(callback_query: types.CallbackQuery, state: FSMContext):
    action = callback_query.data
    user_id = callback_query.from_user.id
    
    if action == settings.ACTIONS.MAIN_MENU:
        await bot_functions.start_function(bot=bot,
                                       user_id=user_id)

    elif settings.ACTIONS.SELECT_WAY in action:
        await bot_functions.select_way_function(bot=bot,
                                                user_id=user_id,
                                                action=action)

    elif settings.ACTIONS.CONFIRM_LOCATION in action:
        await bot_functions.confirm_way_function(bot=bot,
                                                 user_id=user_id,
                                                 action=action)               

    elif settings.ACTIONS.CONFIRM_LISTENED in action:
        await callback_query.message.answer('Вы прослушали аудио!')                                                                                           

    

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
 