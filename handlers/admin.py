from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from confid_data import ADMINS
from create_bot import bot
from data_base import databae_postgre
from keyboards import admin_kb, other_kb


class FSMadmin(StatesGroup):
    photo = State()
    name = State()
    group = State()
    quantity = State()
    user_name = State()


async def commands_start(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.send_message(message.from_user.id, 'система управления складом',
                               reply_markup=admin_kb.button_case_admin)
    else:
        await bot.send_message(message.from_user.id, 'нет доступа')


async def cm_start(message: types.Message):
    await FSMadmin.photo.set()
    await message.reply('add photo')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMadmin.next()
    await message.reply('add name')


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('ok')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMadmin.next()
    await message.reply('add group')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMadmin.next()
    await message.reply('add quantity')


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = int(message.text)
    await FSMadmin.next()
    await message.reply('add your name')


async def loaded_by(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_name'] = message.text

    await databae_postgre.add_info(state)

    await state.finish()
    await bot.send_message(message.from_user.id, 'Что делаем дальше?', reply_markup=other_kb.kb_other)


class FSMdelete(StatesGroup):
    name = State()
    quantity = State()


async def cm_start_delete(message: types.Message):
    await FSMdelete.name.set()
    await message.reply('print name')


async def load_name_delete(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMdelete.next()
    await message.reply('количество')


async def load_quantity_delete(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = int(message.text)
    await databae_postgre.sql_delete_command(state)

    await state.finish()
    await bot.send_message(message.from_user.id, 'Что делаем дальше?', reply_markup=other_kb.kb_other)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['операции'])
    dp.register_message_handler(cm_start, commands=['load'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_name, state=FSMadmin.name)
    dp.register_message_handler(load_group, state=FSMadmin.group)
    dp.register_message_handler(load_quantity, state=FSMadmin.quantity)
    dp.register_message_handler(loaded_by, state=FSMadmin.user_name)
    dp.register_message_handler(cm_start_delete, commands=['delete'])
    dp.register_message_handler(load_name_delete, state=FSMdelete.name)
    dp.register_message_handler(load_quantity_delete, state=FSMdelete.quantity)
