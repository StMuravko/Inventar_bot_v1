import sqlite3 as sq

from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('inventory.db')
    cur = base.cursor()
    if base:
        print('DataBase connected')
    base.execute(
        'CREATE TABLE IF NOT EXISTS inventar(photo TEXT, name TEXT PRIMARY KEY, groups TEXT, quantity INTEGER, loaded_by TEXT)')
    base.commit()


async def sql_add_comand(state):
    async with state.proxy() as data:
        cur.execute(
            f'INSERT INTO inventar VALUES (?,?,?,?,?) ON CONFLICT DO UPDATE SET quantity = quantity + {data["quantity"]};',
            tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM inventar').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\ngroup: {ret[2]}\nquantity: {ret[3]}')


async def sql_read_groups(message):
    for ret in cur.execute('SELECT COUNT(*), groups FROM inventar GROUP BY groups').fetchall():
        await bot.send_message(message.from_user.id, ret)


async def sql_show_by_name(message):
    for ret in cur.execute('SELECT name, quantity FROM inventar ORDER BY name').fetchall():
        await bot.send_message(message.from_user.id, ret)


async def sql_delete_command(state):
    async with state.proxy() as data:
        cur.execute(
            f"UPDATE inventar SET quantity = quantity - {data['quantity']} WHERE inventar.name = '{data['name']}'")
        base.commit()
