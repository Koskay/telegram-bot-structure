from aiogram import Bot
from aiogram import Dispatcher

from config import BOT_TOKEN

#from routes import router

from data_base import settings

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main() -> None:
    if await settings.db_connect():  # Проверка на наличие подключения к базе
        print('database connect')

    #dp.include_router(router)
    await dp.start_polling(bot)
