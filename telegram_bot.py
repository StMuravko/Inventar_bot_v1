from aiogram.utils import executor

from create_bot import dp
from data_base import databae_postgre
from handlers import admin, client, others
APP_TOKEN = "https://git.heroku.com/tgbotsklad.git"


async def on_startup(_):
    print('bot online')
    databae_postgre.create_db()
    print('DB connected')


others.register_handlers_other(dp)
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
