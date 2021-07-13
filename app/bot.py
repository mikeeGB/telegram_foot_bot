import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

import menu_buttons as mb
from configuration.config import TOKEN
from database.db_manager import dbman
from helper_db_funcs import read_tg_id_from_person, write_tg_id_to_db,\
                            write_goals_to_db, write_assists_to_db, check_date_from_team_stats,\
                            update_team_stats,\
                            emptiness_checker,\
                            initialize_team_stats_with_zero,\
                            write_individual_stats_to_match_result_table,\
                            update_stats_games_played,\
                            show_day_individual_stats,\
                            show_all_time_individual_stats,\
                            show_day_team_stats,\
                            show_all_time_team_stats,\
                            show_top_goalscorers_today,\
                            show_top_assistants_today,\
                            show_top_goal_plus_assist_today,\
                            show_top_goalscorers_all_time,\
                            show_top_assistants_all_time,\
                            show_top_goal_plus_assist_all_time


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if message.from_user.id not in read_tg_id_from_person(conn):  # checking for id's in table person
        # adding new player if he clicked /start
        write_tg_id_to_db(conn, message.from_user.id, message.from_user.username)

    if not emptiness_checker(conn):  # fill table team_stats with zeros if table is empty
        initialize_team_stats_with_zero(conn)
    if not check_date_from_team_stats(conn):  # fill table team_stats with zeros if current date is not in table
        initialize_team_stats_with_zero(conn)

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
        write_goals_to_db(conn=conn, goals_num=1,
                          tg_id=message.from_user.id,
                          tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "1x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == '2 Goals: ⚽⚽':
        write_goals_to_db(conn=conn, goals_num=2,
                          tg_id=message.from_user.id,
                          tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "2x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == '3 Goals: ⚽⚽⚽':
        write_goals_to_db(conn=conn, goals_num=3,
                          tg_id=message.from_user.id,
                          tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "3x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == '4 Goals: ⚽⚽⚽⚽':
        write_goals_to_db(conn=conn, goals_num=4,
                          tg_id=message.from_user.id,
                          tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "4x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == '5 Goals: ⚽⚽⚽⚽⚽':
        write_goals_to_db(conn=conn, goals_num=5,
                          tg_id=message.from_user.id,
                          tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "5x⚽", reply_markup=mb.sub_menu_goals_writing)

    elif message.text == 'Завершить матч':
        # ! create additional table match_results to write winnings, defeats, draws
        update_stats_games_played(conn=conn, tg_id=message.from_user.id)
        await bot.send_message(message.from_user.id, "Как закончился матч?",
                               reply_markup=mb.sub_menu_winning_defeat_draw)

    elif message.text == '👊 Победа':
        write_individual_stats_to_match_result_table(conn=conn,
                                                     tg_id=message.from_user.id,
                                                     winnings_num=1,
                                                     defeats_num=0,
                                                     draws_num=0)
        update_team_stats(conn=conn)
        await bot.send_message(message.from_user.id, "Победа записана 🤩",
                               reply_markup=mb.main_menu)

    elif message.text == '🤬 Поражение':
        write_individual_stats_to_match_result_table(conn=conn,
                                                     tg_id=message.from_user.id,
                                                     winnings_num=0,
                                                     defeats_num=1,
                                                     draws_num=0)
        update_team_stats(conn=conn)
        await bot.send_message(message.from_user.id, "Поражение записано 🥺",
                               reply_markup=mb.main_menu)

    elif message.text == '🤝 Ничья':
        write_individual_stats_to_match_result_table(conn=conn,
                                                     tg_id=message.from_user.id,
                                                     winnings_num=0,
                                                     defeats_num=0,
                                                     draws_num=1)
        update_team_stats(conn=conn)
        await bot.send_message(message.from_user.id, "Ничья записана 😐",
                               reply_markup=mb.main_menu)

    elif message.text == 'Записать еще голы':
        await bot.send_message(message.from_user.id, "Записываю еще голы", reply_markup=mb.sub_menu_goals)

    elif message.text == '🅰️ Записать ассисты':
        await bot.send_message(message.from_user.id, "Записываю ассисты", reply_markup=mb.sub_menu_assists)

    elif message.text == '1 Assist: 🎯':
        write_assists_to_db(conn=conn, assists_num=1,
                            tg_id=message.from_user.id,
                            tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "1x🎯", reply_markup=mb.sub_menu_assists_writing)

    elif message.text == '2 Assists: 🎯🎯':
        write_assists_to_db(conn=conn, assists_num=2,
                            tg_id=message.from_user.id,
                            tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "2x🎯", reply_markup=mb.sub_menu_assists_writing)

    elif message.text == '3 Assists: 🎯🎯🎯':
        write_assists_to_db(conn=conn, assists_num=3,
                            tg_id=message.from_user.id,
                            tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "3x🎯", reply_markup=mb.sub_menu_assists_writing)

    elif message.text == '4 Assists: 🎯🎯🎯🎯':
        write_assists_to_db(conn=conn, assists_num=4,
                            tg_id=message.from_user.id,
                            tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "4x🎯", reply_markup=mb.sub_menu_assists_writing)

    elif message.text == '5 Assists: 🎯🎯🎯🎯🎯':
        write_assists_to_db(conn=conn, assists_num=5,
                            tg_id=message.from_user.id,
                            tg_name=message.from_user.username)
        await bot.send_message(message.from_user.id, "5x🎯", reply_markup=mb.sub_menu_assists_writing)

    elif message.text == 'Записать голы':
        await bot.send_message(message.from_user.id, "Записываю голы", reply_markup=mb.sub_menu_goals)

    elif message.text == 'Записать еще ассисты':
        await bot.send_message(message.from_user.id, "Записываю еще ассисты", reply_markup=mb.sub_menu_assists)

    elif message.text == 'Записать ассисты':
        await bot.send_message(message.from_user.id, "Записываю ассисты", reply_markup=mb.sub_menu_assists)

    elif message.text == '↩️Вернуться в меню':
        await bot.send_message(message.from_user.id, "Главное меню", reply_markup=mb.main_menu)

    elif message.text == '↩️Меню выбора статистики':
        await bot.send_message(message.from_user.id, "Меню выбора статистики", reply_markup=mb.sub_menu_stats)

    elif message.text == '🔝 Показать статистику':
        await bot.send_message(message.from_user.id, text='📈 Статистика', reply_markup=mb.sub_menu_stats)

    elif message.text == '🏋️‍♂ Индивидуальная статистика':
        await bot.send_message(message.from_user.id, "Выбор индивидуальной статистики",
                               reply_markup=mb.sub_menu_individual_stats)

    elif message.text == '📅 Моя статистика за сегодня':
        text = f"Ваша статистика за сегодня:\n\n{show_day_individual_stats(conn=conn, tg_id=message.from_user.id)}"
        await message.reply(text, reply_markup=mb.sub_menu_stats, parse_mode=ParseMode.MARKDOWN)

    elif message.text == '🕐 Моя статистика за все время':
        text = f"Ваша статистика за все время:\n\n" \
               f"{show_all_time_individual_stats(conn=conn, tg_id=message.from_user.id)}"
        await message.reply(text, reply_markup=mb.sub_menu_stats, parse_mode=ParseMode.MARKDOWN)

    elif message.text == '🏆 Командная статистика':
        await bot.send_message(message.from_user.id, "Выбор командной статистики",
                               reply_markup=mb.sub_menu_team_stats)

    elif message.text == '🍅 Командная статистика за сегодня':
        text = f"Командная статистика за сегодня:\n\n{show_day_team_stats(conn=conn)}"
        await message.reply(text, reply_markup=mb.sub_menu_stats, parse_mode=ParseMode.MARKDOWN)

    elif message.text == '🥒 Командная статистика за все время':
        text = f"Командная статистика за все время:\n\n{show_all_time_team_stats(conn=conn)}"
        await message.reply(text, reply_markup=mb.sub_menu_stats, parse_mode=ParseMode.MARKDOWN)

    elif message.text == '🥇 Топ лучших игроков':
        await bot.send_message(message.from_user.id, "Топ игроков", reply_markup=mb.sub_menu_top)

    elif message.text == '🔝 за сегодня':
        await bot.send_message(message.from_user.id, "Топ за сегодня",
                               reply_markup=mb.sub_menu_top_players_today_stats)

    elif message.text == '🔝 за все время':
        await bot.send_message(message.from_user.id, "Топ за все время",
                               reply_markup=mb.sub_menu_top_players_all_time_stats)

    elif message.text == '↩️Меню командной статистики':
        await bot.send_message(message.from_user.id, "Командная статистика", reply_markup=mb.sub_menu_team_stats)

    # today top player stats
    elif message.text == '🔫 Топ бомбардиров':
        text = f"Топ бомбардиров за сегодня:\n\n{show_top_goalscorers_today(conn=conn)}"
        await message.reply(text, reply_markup=mb.sub_menu_top_players_today_stats)

    elif message.text == '👠 Топ ассистентов':
        text = f"Топ ассистентов за сегодня:\n\n{show_top_assistants_today(conn=conn)}"
        await message.reply(text, reply_markup=mb.sub_menu_top_players_today_stats)

    elif message.text == '🔫️👠 Топ гол + пас':
        text = f"Топ игроков по системе гол+пас за сегодня:\n\n{show_top_goal_plus_assist_today(conn=conn)}"
        await message.reply(text, reply_markup=mb.sub_menu_top_players_today_stats)

    # all time top player stats
    elif message.text == '💣 Топ бомбардиров':
        text = f"Топ бомбардиров за все время:\n\n{show_top_goalscorers_all_time(conn=conn)}"
        await message.reply(text, reply_markup=mb.sub_menu_top_players_all_time_stats)

    elif message.text == '🎯 Топ ассистентов':
        text = f"Топ ассистентов за все время:\n\n{show_top_assistants_all_time(conn=conn)}"
        await message.reply(text, reply_markup=mb.sub_menu_top_players_all_time_stats)

    elif message.text == '💣🎯 Топ гол + пас':
        text = f"Топ игроков по системе гол+пас за все время:\n\n{show_top_goal_plus_assist_all_time(conn=conn)}"
        await message.reply(text, reply_markup=mb.sub_menu_top_players_all_time_stats)

    else:
        await message.reply("Такой команды не существует. Нажмите /start для отображения меню")

if __name__ == '__main__':
    conn = dbman.create_connection()
    executor.start_polling(dispatcher=dp, skip_updates=True)
