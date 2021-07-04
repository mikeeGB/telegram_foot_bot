import datetime
from database.db_manager import dbman
from queries_templates import ADDING_PLAYER_Q, SELECT_TG_ID_FROM_PERSONS, ADD_GOALS, UPDATE_GOALS, \
                              SELECT_DATE_FROM_STATS


def read_tg_id_from_person(conn):
    data_id = dbman.execute_read_query(conn, SELECT_TG_ID_FROM_PERSONS)
    res = list(map(lambda x: x[0], data_id))
    print(res)
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
