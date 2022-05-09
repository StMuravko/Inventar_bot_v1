from aiogram import types, Dispatcher

from data_base import databae_postgre
from confid_data import ADMINS
from create_bot import bot
from keyboards import kb_client
from keyboards.other_kb import kb_other


async def commands_start(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.send_message(message.from_user.id, 'Выберите сортировку по товару на складе', reply_markup=kb_client)
    else:
       await bot.send_message(message.from_user.id,'нет доступа')


async def show_inventar(message: types.Message):
    if message.from_user.id in ADMINS:
        await databae_postgre.check_db(message)
        await bot.send_message(message.from_user.id, 'Это все то есть на складе', reply_markup=kb_other)


async def show_by_group(message: types.Message):
    if message.from_user.id in ADMINS:
        await databae_postgre.sql_read_groups(message)
        await bot.send_message(message.from_user.id, 'Это все то есть на складе', reply_markup=kb_other)



async def show_by_name(message: types.Message):
    if message.from_user.id in ADMINS:
        await databae_postgre.sql_show_by_name(message)
        await bot.send_message(message.from_user.id, 'Это все то есть на складе', reply_markup=kb_other)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['склад'])
    dp.register_message_handler(show_inventar, commands=['показать_все'])
    dp.register_message_handler(show_by_group, commands=['сортировка_по_группам'])
    dp.register_message_handler(show_by_name, commands=['сортировка_по_наименованию'])
