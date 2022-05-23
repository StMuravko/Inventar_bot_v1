from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_load = KeyboardButton('/добавить')
button_delete = KeyboardButton('/удалить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)
