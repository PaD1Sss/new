from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN')) # Читаем токен
dp: Dispatcher = Dispatcher(bot, storage=storage) # Инициализируем диспечера
