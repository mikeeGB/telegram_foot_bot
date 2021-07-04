ADDING_PLAYER_Q = "INSERT INTO person(tg_id, tg_name) VALUES({tg_id}, {tg_name})"
SELECT_TG_ID_FROM_PERSONS = "SELECT tg_id FROM person"
ADD_GOALS = """INSERT INTO
                          stats(goals, assists, games_played, tg_id, tg_name)
                        VALUES({goals_num}, 0, 0, (SELECT tg_id FROM person WHERE tg_id = {cur_tg_id}),
                               (SELECT tg_name FROM person WHERE tg_name = {cur_tg_name}))"""
