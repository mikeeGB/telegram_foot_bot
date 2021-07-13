import datetime

from aiogram.utils.markdown import bold, text, escape_md

from database.db_manager import dbman
from queries_templates import ADDING_PLAYER_Q, SELECT_TG_ID_FROM_PERSONS, ADD_GOALS, UPDATE_GOALS, \
                              SELECT_DATE_FROM_STATS, ADD_ASSISTS, UPDATE_ASSISTS,\
                              INITIALIZE_TEAM_STATS_WITH_ZERO, UPDATE_CUR_DATE_TEAM_STATS,\
                              SELECT_DATE_FROM_TEAM_STATS, CHECK_TEAM_STATS_TABLE_EMPTINESS,\
                              INSERT_INTO_MATCH_RESULTS_TABLE,\
                              UPDATE_GAMES_PLAYED_IN_STATS_TABLE,\
                              SELECT_DAY_STATS_INDIVIDUAL,\
                              SELECT_ALL_TIME_INDIVIDUAL_STATS,\
                              SELECT_TEAM_STATS_TODAY_WITH_AVG,\
                              SELECT_TEAM_STATS_ALL_TIME_WITH_AVG,\
                              SELECT_GAMES_PLAYED_FROM_TEAM_STATS_ALL_TIME,\
                              SELECT_GAMES_PLAYED_FROM_TEAM_STATS_TODAY,\
                              SELECT_TOP_GOALSCORERS_TODAY,\
                              SELECT_TOP_ASSISTANTS_TODAY,\
                              SELECT_TOP_GOAL_PLUS_ASSIST_TODAY,\
                              SELECT_TOP_GOALSCORERS_ALL_TIME,\
                              SELECT_TOP_ASSISTANTS_ALL_TIME,\
                              SELECT_TOP_GOAL_PLUS_ASSIST_ALL_TIME


def read_tg_id_from_person(conn):
    data_id = dbman.execute_read_query(conn, SELECT_TG_ID_FROM_PERSONS)
    res = list(map(lambda x: x[0], data_id))
    return res


def write_tg_id_to_db(conn, user_id, user_name):
    add_player_query = ADDING_PLAYER_Q.format(tg_id=user_id,
                                              tg_name=f"'{user_name}'")
    dbman.execute_query(conn, add_player_query)
    conn.commit()  # commit changes


def write_goals_to_db(conn, goals_num, tg_id, tg_name):
    if check_date_from_stats(conn, tg_id):  # if current date is in db, use UPDATE
        update_goals_in_db(conn, goals_num, tg_id)
    else:
        add_goals_query = ADD_GOALS.format(cur_tg_id=tg_id,
                                           goals_num=goals_num,
                                           cur_tg_name=f"'{tg_name}'")
        dbman.execute_query(conn, add_goals_query)
        conn.commit()


def update_goals_in_db(conn, goals_num, tg_id):
    update_goals_query = UPDATE_GOALS.format(goals_num=goals_num,
                                             cur_tg_id=tg_id)
    dbman.execute_query(conn, update_goals_query)
    conn.commit()


def check_date_from_stats(conn, tg_id):
    select_date_query = SELECT_DATE_FROM_STATS.format(cur_tg_id=tg_id)
    date_from_stats = dbman.execute_read_query(conn, select_date_query)
    res = list(map(lambda x: x[0], date_from_stats))
    return datetime.date.today() in res


def write_assists_to_db(conn, assists_num, tg_id, tg_name):
    if check_date_from_stats(conn, tg_id):  # if current date is in db, use UPDATE
        update_assists_in_db(conn, assists_num, tg_id)
    else:
        add_assists_query = ADD_ASSISTS.format(cur_tg_id=tg_id,
                                               assists_num=assists_num,
                                               cur_tg_name=f"'{tg_name}'")
        dbman.execute_query(conn, add_assists_query)
        conn.commit()


def update_assists_in_db(conn, assists_num, tg_id):
    update_assists_query = UPDATE_ASSISTS.format(assists_num=assists_num,
                                                 cur_tg_id=tg_id)
    dbman.execute_query(conn, update_assists_query)
    conn.commit()


def initialize_team_stats_with_zero(conn):
    dbman.execute_query(conn, INITIALIZE_TEAM_STATS_WITH_ZERO)
    conn.commit()


def check_date_from_team_stats(conn):
    date_from_team_stats = dbman.execute_read_query(conn, SELECT_DATE_FROM_TEAM_STATS)
    return datetime.date.today() in date_from_team_stats[-1]  # compares current date and last date in table


def update_team_stats(conn):
    if check_date_from_team_stats(conn):  # if current date is in table
        dbman.execute_query(conn, UPDATE_CUR_DATE_TEAM_STATS)  # update team stats
        conn.commit()
    else:
        initialize_team_stats_with_zero(conn)  # else - insert new row with zeros


def emptiness_checker(conn):
    x = dbman.execute_read_query(conn, CHECK_TEAM_STATS_TABLE_EMPTINESS)
    return x[0][0]


def write_individual_stats_to_match_result_table(conn, tg_id, winnings_num, defeats_num, draws_num):
    insert_into_match_res_query = INSERT_INTO_MATCH_RESULTS_TABLE.format(tg_user_id=tg_id,
                                                                         winnings_num=winnings_num,
                                                                         defeats_num=defeats_num,
                                                                         draws_num=draws_num)
    dbman.execute_query(conn, insert_into_match_res_query)
    conn.commit()


def update_stats_games_played(conn, tg_id):
    update_games_played_query = UPDATE_GAMES_PLAYED_IN_STATS_TABLE.format(tg_user_id=tg_id)
    dbman.execute_query(conn, update_games_played_query)
    conn.commit()


def select_day_individual_stats(conn, tg_id):
    select_day_ind_stats_query = SELECT_DAY_STATS_INDIVIDUAL.format(tg_user_id=tg_id)
    day_stats_ind_tuple = dbman.execute_read_query(conn, select_day_ind_stats_query)
    if day_stats_ind_tuple:
        return day_stats_ind_tuple[0]
    return "Нет статистики за сегодня"


def show_day_individual_stats(conn, tg_id):
    data = select_day_individual_stats(conn, tg_id)
    if type(data) is tuple:
        message_text = text(bold("Дата:"), f"{data[0]}",
                            bold("Игрок:"), escape_md(f"{data[1]}"),
                            bold("Игр сыграно:"), f"{data[2]}",
                            bold("Голы:"), f"{data[3]}",
                            bold("Ассисты:"), f"{data[4]}",
                            "\n---------------------------------------------",
                            "В среднем за матч:\n",
                            bold("Голов:"), f"{data[5]}",
                            bold("Ассистов:"), f"{data[6]}", sep='\n')

    else:
        message_text = data
    return message_text


def select_all_time_individual_stats(conn, tg_id):
    select_all_time_ind_stats_query = SELECT_ALL_TIME_INDIVIDUAL_STATS.format(tg_user_id=tg_id)
    all_time_stats_tuple = dbman.execute_read_query(conn, select_all_time_ind_stats_query)
    if all_time_stats_tuple:
        return all_time_stats_tuple[0]
    return "Еще нет статистики"


def show_all_time_individual_stats(conn, tg_id):
    data = select_all_time_individual_stats(conn, tg_id)
    if type(data) is tuple:
        message_text = text(bold("Период:"), f"{data[1]} --> {data[2]}",
                            bold("Игрок:"), escape_md(f"{data[0]}"),
                            bold("Игр сыграно:"), f"{data[3]}",
                            bold("Результативные игровые дни:"), f"{data[4]}",
                            bold("Голы:"), f"{data[5]}",
                            bold("Ассисты:"), f"{data[6]}",
                            "\n---------------------------------------------",
                            "В среднем за матч:\n",
                            bold("Голов:"), f"{data[7]}",
                            bold("Ассистов:"), f"{data[8]}", sep='\n')

    else:
        message_text = data
    return message_text


def select_day_team_stats(conn):
    select_games_played_query = SELECT_GAMES_PLAYED_FROM_TEAM_STATS_TODAY
    games_played_tuple = dbman.execute_read_query(conn, select_games_played_query)
    if games_played_tuple and games_played_tuple[0][0] != 0:
        select_day_team_stats_query = SELECT_TEAM_STATS_TODAY_WITH_AVG
        day_stats_team_tuple = dbman.execute_read_query(conn, select_day_team_stats_query)
        return day_stats_team_tuple[0]
    return "Нет статистики за сегодня"


def show_day_team_stats(conn):
    data = select_day_team_stats(conn)
    if type(data) is tuple:
        message_text = text(bold("Дата:"), f"{data[0]}",
                            bold("Игр сыграно:"), f"{data[1]}",
                            bold("Голы:"), f"{data[2]}",
                            bold("Ассисты:"), f"{data[3]}",
                            bold("Победы:"), f"{data[4]}",
                            bold("Поражения:"), f"{data[5]}",
                            bold("Ничейные результаты:"), f"{data[6]}",
                            "\n---------------------------------------------",
                            "В среднем за матч:\n",
                            bold("Голов:"), f"{data[7]}",
                            bold("Ассистов:"), f"{data[8]}",
                            bold("Побед:"), f"{data[9]}",
                            bold("Поражений:"), f"{data[10]}",
                            bold("Ничей:"), f"{data[11]}", sep='\n')

    else:
        message_text = data
    return message_text


def select_all_time_team_stats(conn):
    select_games_played_query = SELECT_GAMES_PLAYED_FROM_TEAM_STATS_ALL_TIME
    games_played_tuple = dbman.execute_read_query(conn, select_games_played_query)
    if games_played_tuple and games_played_tuple[0][0] != 0:
        select_all_time_team_stats_query = SELECT_TEAM_STATS_ALL_TIME_WITH_AVG
        all_time_stats_team_tuple = dbman.execute_read_query(conn, select_all_time_team_stats_query)
        return all_time_stats_team_tuple[0]
    return "Нет статистики за сегодня"


def show_all_time_team_stats(conn):
    data = select_all_time_team_stats(conn)
    if type(data) is tuple:
        message_text = text(bold("Период:"), f"{data[0]} --> {data[1]}",
                            bold("Игр сыграно:"), f"{data[2]}",
                            bold("Голы:"), f"{data[3]}",
                            bold("Ассисты:"), f"{data[4]}",
                            bold("Победы:"), f"{data[5]}",
                            bold("Поражения:"), f"{data[6]}",
                            bold("Ничейные результаты:"), f"{data[7]}",
                            "\n---------------------------------------------",
                            "В среднем за матч:\n",
                            bold("Голов:"), f"{data[8]}",
                            bold("Ассистов:"), f"{data[9]}",
                            bold("Побед:"), f"{data[10]}",
                            bold("Поражений:"), f"{data[11]}",
                            bold("Ничей:"), f"{data[12]}", sep='\n')

    else:
        message_text = data
    return message_text


def select_top_goalscorers_today(conn):
    select_top_goalscorers_today_query = SELECT_TOP_GOALSCORERS_TODAY
    top_today_goalscorers_data = dbman.execute_read_query(conn, select_top_goalscorers_today_query)
    if top_today_goalscorers_data:
        return top_today_goalscorers_data
    return "Нет статистики за сегодня"


def show_top_goalscorers_today(conn):
    data = select_top_goalscorers_today(conn)
    if type(data) is not str:
        message_text = f"Дата: {datetime.date.today()}\n"
        for i, data_tuple in enumerate(data):
            message_text += f"{i+1}) {data_tuple[0]} - {data_tuple[1]}x⚽\n"
    else:
        message_text = data
    return message_text


def select_top_assistants_today(conn):
    select_top_assistants_today_query = SELECT_TOP_ASSISTANTS_TODAY
    top_today_assistants_data = dbman.execute_read_query(conn, select_top_assistants_today_query)
    if top_today_assistants_data:
        return top_today_assistants_data
    return "Нет статистики за сегодня"


def show_top_assistants_today(conn):
    data = select_top_assistants_today(conn)
    if type(data) is not str:
        message_text = f"Дата: {datetime.date.today()}\n"
        for i, data_tuple in enumerate(data):
            message_text += f"{i+1}) {data_tuple[0]} - {data_tuple[1]}x🎯\n"
    else:
        message_text = data
    return message_text


def select_top_goal_plus_assist_today(conn):
    select_top_goal_plus_assist_today_query = SELECT_TOP_GOAL_PLUS_ASSIST_TODAY
    top_today_goal_plus_assist_data = dbman.execute_read_query(conn, select_top_goal_plus_assist_today_query)
    if top_today_goal_plus_assist_data:
        return top_today_goal_plus_assist_data
    return "Нет статистики за сегодня"


def show_top_goal_plus_assist_today(conn):
    data = select_top_goal_plus_assist_today(conn)
    if type(data) is not str:
        message_text = f"Дата: {datetime.date.today()}\n"
        for i, data_tuple in enumerate(data):
            message_text += f"{i+1}) {data_tuple[0]} - {data_tuple[1]} points\n"
    else:
        message_text = data
    return message_text


def select_top_goalscorers_all_time(conn):
    select_top_goalscorers_all_time_query = SELECT_TOP_GOALSCORERS_ALL_TIME
    top_all_time_goalscorers_data = dbman.execute_read_query(conn, select_top_goalscorers_all_time_query)
    if top_all_time_goalscorers_data:
        return top_all_time_goalscorers_data
    return "Нет статистики за сегодня"


def show_top_goalscorers_all_time(conn):
    data = select_top_goalscorers_all_time(conn)
    if type(data) is not str:
        message_text = ""
        for i, data_tuple in enumerate(data):
            message_text += f"{i+1}) {data_tuple[0]} - {data_tuple[1]}x⚽\n"
    else:
        message_text = data
    return message_text


def select_top_assistants_all_time(conn):
    select_top_assistants_all_time_query = SELECT_TOP_ASSISTANTS_ALL_TIME
    top_all_time_assistants_data = dbman.execute_read_query(conn, select_top_assistants_all_time_query)
    if top_all_time_assistants_data:
        return top_all_time_assistants_data
    return "Нет статистики за сегодня"


def show_top_assistants_all_time(conn):
    data = select_top_assistants_all_time(conn)
    if type(data) is not str:
        message_text = ""
        for i, data_tuple in enumerate(data):
            message_text += f"{i+1}) {data_tuple[0]} - {data_tuple[1]}x🎯\n"
    else:
        message_text = data
    return message_text


def select_top_goal_plus_assist_all_time(conn):
    select_top_goal_plus_assist_all_time_query = SELECT_TOP_GOAL_PLUS_ASSIST_ALL_TIME
    top_all_time_goal_plus_assist_data = dbman.execute_read_query(conn, select_top_goal_plus_assist_all_time_query)
    if top_all_time_goal_plus_assist_data:
        return top_all_time_goal_plus_assist_data
    return "Нет статистики за сегодня"


def show_top_goal_plus_assist_all_time(conn):
    data = select_top_goal_plus_assist_all_time(conn)
    if type(data) is not str:
        message_text = ""
        for i, data_tuple in enumerate(data):
            message_text += f"{i+1}) {data_tuple[0]} - {data_tuple[1]} points\n"
    else:
        message_text = data
    return message_text
