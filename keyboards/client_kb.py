from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/show_all')
b2 = KeyboardButton('/show_groups')
b3 = KeyboardButton('/show_names')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).add(b3)
