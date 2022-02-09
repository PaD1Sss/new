from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text

from data_base import sqlite_db
from keyboarsd import kb_client

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# # Получаем ID текущего модератора

# Начало диалога загрузки нового пункта меню
# @dp.message_handler(commands='Продать_Квартиру?', state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузить фото')


# ВЫхд из состояния
# @dp.register_message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


# Ловим первый ответ от пользователя
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Теперь введи адресс")


# Ловим второй ответ пользователя(описание)
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите описание")


# Ловим 3 ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply("Теперь укажи цену")


# ловим ответ 4 (цена)
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
        await bot.send_message(message.from_user.id, text="Запись добавлена", reply_markup=kb_client)

    await sqlite_db.sql_add_command(state)

    await state.finish()


# Регистрируем хэндлеры

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Продать_Квартиру?'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
