import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import menu_buttons as mb
from configuration.config import TOKEN
from database.db_manager import dbman
from queries_templates import ADDING_PLAYER_Q, SELECT_TG_ID_FROM_PERSONS


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def read_tg_id_from_person():
    data_id = dbman.execute_read_query(conn, SELECT_TG_ID_FROM_PERSONS)
    res = list(map(lambda x: x[0], data_id))
    print(res)
    return res


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):

    if message.from_user.id not in read_tg_id_from_person():  # checking for id's in table person
        # adding new player if he clicked /start
        add_player_query = ADDING_PLAYER_Q.format(tg_id=message.from_user.id,
                                                  tg_name=f"'{message.from_user.username}'")

        dbman.execute_query(conn, add_player_query)
        conn.commit()  # commit changes
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.username}!",
                           reply_markup=mb.main_menu)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Введите /start для отображения меню")


@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == '⚽ Записать голы':
        await bot.send_message(message.from_user.id, '⚽ Записываю',
                               reply_markup=mb.sub_menu_goals)
    elif message.text == '1 Goal: ⚽':
        await bot.send_message(message.from_user.id, "1x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == '2 Goals: ⚽⚽':
        await bot.send_message(message.from_user.id, "2x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == '3 Goals: ⚽⚽⚽':
        await bot.send_message(message.from_user.id, "3x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == '4 Goals: ⚽⚽⚽⚽':
        await bot.send_message(message.from_user.id, "4x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == '5 Goals: ⚽⚽⚽⚽⚽':
        await bot.send_message(message.from_user.id, "5x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == 'Завершить матч':
        await bot.send_message(message.from_user.id, "Матч завершен", reply_markup=mb.main_menu)

    elif message.text == 'Записать еще голы':
        await bot.send_message(message.from_user.id, "Записываю еще голы", reply_markup=mb.sub_menu_goals)


if __name__ == '__main__':
    conn = dbman.create_connection()
    executor.start_polling(dispatcher=dp, skip_updates=True)
