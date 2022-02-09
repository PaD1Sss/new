from aiogram import types

from data_base.sqlite_db import sql_read


async def start_key():
    l = await sql_read()
    keyboard = types.InlineKeyboardMarkup()
    button_menu = [types.InlineKeyboardButton(text=str(x), callback_data=str(x)) for x in l]
    keyboard.add(*button_menu)
    return keyboard
