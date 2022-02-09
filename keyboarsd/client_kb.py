from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove



b1 = KeyboardButton('/Купить_Квартиру?')
b2 = KeyboardButton('/Продать_Квартиру?')
# b4 = KeyboardButton('/Поделиться номером', request_contact=True)
# b5 = KeyboardButton('/Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2)  # .row(b4, b5)
