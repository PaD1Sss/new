from data_base.config import ADMINS
from aiogram import Dispatcher
from create_bot import bot as bt
x = ADMINS


async def on_startup_notify():
    await bt.send_message(x, "Бот Запущен")
