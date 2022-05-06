from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5367853662:AAFpR2vp7BWsBVwIiyrPHzOIcjmdkeOv8eo')
dp = Dispatcher(bot, storage=storage)

