import sqlite3 as sq

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from create_bot import bot
from data_base.config import ADMINS



def sql_start():
    global base, cur
    base = sq.connect('pizza1_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT OR REPLACE INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read():
    for x in cur.execute('SELECT name FROM menu').fetchall():
        for y in range(len(x)):
            return x
            # search_name.append(x[y])

    # some_list = []
    # for i in cur.execute('SELECT name FROM menu').fetchall():
    #     for x in range(len[i]):
    #         some_list.append(i[x])


#
# async def sql_add_adr(message):
#     await add_adr(message)
#     return cur.execute('SELECT name FROM menu').fetchall()


# keyboard = InlineKeyboardMarkup()
# keyboard.row_width = 1
# keyboard.add(InlineKeyboardButton(text=ret[i], callback_data='ad'))
#
# await bot.send_message(message.from_user.id, text='ул.', reply_markup=keyboard)
delete_cmd = []


async def sql_read2(message, data):
    for par1 in cur.execute('SELECT * FROM menu WHERE name == ?', (data,)):
        await bot.send_photo(message.from_user.id, par1[0], f'{par1[1]}\nОписание: {par1[2]}\nЦена {par1[-1]}')
        if message.from_user.id == ADMINS:
            inline_btn_1 = InlineKeyboardButton(text='Удалить!', callback_data='delete_btn')
            inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
            await bot.send_message(message.from_user.id, text='^^^^', reply_markup=inline_kb1)


async def sql_read3(message):
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data[0],))
    base.commit()
    delete_cmd.clear()
