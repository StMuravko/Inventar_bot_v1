from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/операции')
b2 = KeyboardButton('/склад')


kb_other = ReplyKeyboardMarkup(resize_keyboard=True).add(b1).add(b2)