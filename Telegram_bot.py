
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from utils.notify_admin import on_startup_notify


async def on_startup(_):
    await on_startup_notify()
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()




from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
