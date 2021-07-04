from database.db_manager import dbman
from queries_templates import ADDING_PLAYER_Q, SELECT_TG_ID_FROM_PERSONS


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
