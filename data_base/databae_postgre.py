import psycopg2

from confid_data import BD_URL
from create_bot import bot

# base = psycopg2.connect(BD_URL)
# cur = base.cursor()


def create_db():
    global base, cur
    base = psycopg2.connect(BD_URL)
    cur = base.cursor()
    if base:
        print('Connection>>>')
        cur.execute(
            "CREATE TABLE IF NOT EXISTS inventar(photo TEXT, name TEXT PRIMARY KEY, groups TEXT, quantity INTEGER, loaded_by TEXT)"
        )
        base.commit()
        print('Done')


async def add_info(state):
    async with state.proxy() as data:
        cur.execute(
            f"INSERT INTO inventar VALUES (%s,%s,%s,%s,%s) ON CONFLICT (name) DO UPDATE SET quantity = inventar.quantity + {data['quantity']};",
            tuple(data.values()))
        base.commit()


async def check_db(message):
    cur.execute(
        "SELECT * FROM inventar;"
    )
    for ret in cur.fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\ngroup: {ret[2]}\nquantity: {ret[3]}')


async def sql_read_groups(message):
    cur.execute(
        "SELECT COUNT(*), groups FROM inventar GROUP BY groups"
    )
    for ret in cur.fetchall():
        await bot.send_message(message.from_user.id, ret)


async def sql_show_by_name(message):
    cur.execute(
        "SELECT name, quantity FROM inventar ORDER BY name"
    )
    for ret in cur.fetchall():
        await bot.send_message(message.from_user.id, ret)


async def sql_delete_command(state):
    async with state.proxy() as data:
        cur.execute(
            f"UPDATE inventar SET quantity = inventar.quantity -  {data['quantity']} WHERE inventar.name = '{data['name']}';"
        )
    base.commit()
