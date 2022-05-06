from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_other


async def start_comand(message: types.Message):
    await bot.send_message(message.from_user.id, 'Слава Украине', reply_markup=kb_other)



def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(start_comand, commands=['start'])