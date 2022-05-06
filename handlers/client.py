from aiogram import types, Dispatcher

from create_bot import bot
from data_base import sqlite_db
from keyboards import kb_client



async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите сортировку по товару на складе', reply_markup=kb_client)


async def show_inventar(message: types.Message):
    await sqlite_db.sql_read(message)

async def show_by_group(message: types.Message):
    await sqlite_db.sql_read_groups(message)

async def show_by_name(message : types.Message):
    await sqlite_db.sql_show_by_name(message)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['склад'])
    dp.register_message_handler(show_inventar, commands=['show_all'])
    dp.register_message_handler(show_by_group, commands=['show_groups'])
    dp.register_message_handler(show_by_name, commands=['show_names'])
