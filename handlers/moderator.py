from aiogram import types

from create_bot import dp
from filters import IsPrivate


@dp.message_handler(IsPrivate(), user_id=[1334853216], text="secret")
async def admin_chat_secret(message: types.Message):
    await message.answer("Вы вошли в меню Админов")
