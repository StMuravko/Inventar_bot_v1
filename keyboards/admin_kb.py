from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_load = KeyboardButton('/load')
button_delete = KeyboardButton('/delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)
