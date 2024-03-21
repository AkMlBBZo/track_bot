import settings
import bot_functions

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=settings.BOT_TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot_functions.start_function(bot=bot,
                                       user_id=message.from_user.id)
    

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
 