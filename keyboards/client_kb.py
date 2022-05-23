from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/показать_все')
b2 = KeyboardButton('/сортировка_по_группам')
b3 = KeyboardButton('/сортировка_по_наименованию')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).add(b3)
