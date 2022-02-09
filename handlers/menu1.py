from aiogram import types, Dispatcher
from create_bot import bot
# @dp.message_handler(commands=['Купить_Квартиру?'])
from keyboarsd.inline import start_key


async def process_command_1(message: types.Message):
    text = 'Выберите адрес'
    keyboard = await start_key()
    await bot.send_message(message.chat.id, text=text, reply_markup=keyboard)



