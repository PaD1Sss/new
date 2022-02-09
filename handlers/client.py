from aiogram import types, Dispatcher
from create_bot import bot
from handlers.menu1 import process_command_1
from keyboarsd import kb_client


## @dp.message_handler(commands=['start', 'help']) # Команда по которой отвечает бот


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здраствуйте, Я бот РИЭЛТОР',
                               reply_markup=kb_client)  # Отправляем в л/с смс
        await message.delete()
    except:
        await message.reply(
            'Общение с ботом через Л/С, напите ему:\nhttps://t.me/PaD1STBot')  # Упомянул смс что писать надо в лс


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(process_command_1, commands=['Купить_Квартиру?'])
