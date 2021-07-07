ADDING_PLAYER_Q = "INSERT INTO person(tg_id, tg_name) VALUES({tg_id}, {tg_name})"
SELECT_TG_ID_FROM_PERSONS = "SELECT tg_id FROM person"
ADD_GOALS = """INSERT INTO
                          stats(goals, assists, games_played, tg_id, tg_name)
                        VALUES({goals_num}, 0, 0, (SELECT tg_id FROM person WHERE tg_id = {cur_tg_id}),
                               (SELECT tg_name FROM person WHERE tg_name = {cur_tg_name}));"""

UPDATE_GOALS = """UPDATE stats
                    SET goals = goals + {goals_num}
                    WHERE tg_id = {cur_tg_id} AND cur_date = CURRENT_DATE;
                  """

SELECT_DATE_FROM_STATS = "SELECT cur_date FROM stats WHERE tg_id = {cur_tg_id}"

ADD_ASSISTS = """INSERT INTO
                          stats(goals, assists, games_played, tg_id, tg_name)
                        VALUES(0, {assists_num}, 0, (SELECT tg_id FROM person WHERE tg_id = {cur_tg_id}),
                               (SELECT tg_name FROM person WHERE tg_name = {cur_tg_name}));"""

UPDATE_ASSISTS = """UPDATE stats
                        SET assists = assists + {assists_num}
                        WHERE tg_id = {cur_tg_id} AND cur_date = CURRENT_DATE;"""

INITIALIZE_TEAM_STATS_WITH_ZERO = """INSERT INTO 
                                        team_stats(games_played, goals, assists, winnings, defeats, draws)
                                      VALUES(0, 0, 0, 0, 0, 0);"""

UPDATE_CUR_DATE_TEAM_STATS = """UPDATE team_stats
                                SET games_played = (SELECT SUM(games_played) FROM stats
                                                    WHERE tg_id = 452975280 AND cur_date = CURRENT_DATE),
                                    goals = (SELECT SUM(goals) FROM stats WHERE cur_date = CURRENT_DATE),
                                    assists = (SELECT SUM(assists) FROM stats WHERE cur_date = CURRENT_DATE),
                                    winnings = 0,
                                    defeats = 0,
                                    draws = 0
                                WHERE cur_date = CURRENT_DATE;"""

SELECT_DATE_FROM_TEAM_STATS = """SELECT cur_date FROM team_stats"""

CHECK_TEAM_STATS_TABLE_EMPTINESS = """SELECT(EXISTS(SELECT * FROM team_stats))"""

INSERT_INTO_MATCH_RESULTS_TABLE = """INSERT INTO match_results(tg_id, winnings, defeats, draws)
                                            VALUES({tg_user_id}, {winnings_num}, {defeats_num}, {draws_num});"""

UPDATE_GAMES_PLAYED_IN_STATS_TABLE = """UPDATE stats
                                        SET games_played = games_played + 1
                                        WHERE tg_id = {tg_user_id} AND cur_date = CURRENT_DATE;"""
