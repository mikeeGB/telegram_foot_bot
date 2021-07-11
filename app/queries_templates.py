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
                                    winnings = (SELECT SUM(winnings) FROM match_results WHERE cur_date = CURRENT_DATE
                                                                                        AND tg_id = 452975280),
                                    defeats = (SELECT SUM(defeats) FROM match_results WHERE cur_date = CURRENT_DATE
                                                                                        AND tg_id = 452975280),
                                    draws = (SELECT SUM(draws) FROM match_results WHERE cur_date = CURRENT_DATE
                                                                                        AND tg_id = 452975280)
                                WHERE cur_date = CURRENT_DATE;"""

SELECT_DATE_FROM_TEAM_STATS = """SELECT cur_date FROM team_stats"""

CHECK_TEAM_STATS_TABLE_EMPTINESS = """SELECT(EXISTS(SELECT * FROM team_stats))"""

INSERT_INTO_MATCH_RESULTS_TABLE = """INSERT INTO match_results(tg_id, winnings, defeats, draws)
                                            VALUES({tg_user_id}, {winnings_num}, {defeats_num}, {draws_num});"""

UPDATE_GAMES_PLAYED_IN_STATS_TABLE = """UPDATE stats
                                        SET games_played = games_played + 1
                                        WHERE tg_id = {tg_user_id} AND cur_date = CURRENT_DATE;"""

SELECT_DAY_STATS_INDIVIDUAL = """SELECT cur_date, tg_name, games_played, goals, assists,
                                 ROUND((CAST(goals AS numeric) / CAST(games_played AS numeric)), 2),
                                 ROUND((CAST(assists AS numeric) / CAST(games_played AS numeric)), 2)
                                    FROM stats
                                 WHERE cur_date = CURRENT_DATE AND tg_id = {tg_user_id};"""

SELECT_ALL_TIME_INDIVIDUAL_STATS = """SELECT tg_name, MIN(cur_date), MAX(cur_date), SUM(games_played), COUNT(cur_date),
                                                      SUM(goals), SUM(assists), 
                                          ROUND(CAST(SUM(goals) AS numeric) / CAST(SUM(games_played) AS numeric), 2),
                                          ROUND(CAST(SUM(assists) AS numeric) / CAST(SUM(games_played) AS numeric), 2)         
                                        FROM stats
                                        WHERE tg_id = {tg_user_id}
                                        GROUP BY tg_name;"""

SELECT_TEAM_STATS_TODAY_WITH_AVG = """SELECT cur_date, games_played, goals, assists, winnings, defeats, draws,
                                    ROUND((CAST(goals AS numeric) / CAST(games_played AS numeric)), 2),
                                    ROUND((CAST(assists AS numeric) / CAST(games_played AS numeric)), 2),
                                    ROUND((CAST(winnings AS numeric) / CAST(games_played AS numeric)), 2),
                                    ROUND((CAST(defeats AS numeric) / CAST(games_played AS numeric)), 2),
                                    ROUND((CAST(draws AS numeric) / CAST(games_played AS numeric)), 2)
                                FROM team_stats
                             WHERE cur_date = CURRENT_DATE;"""

SELECT_TEAM_STATS_ALL_TIME_WITH_AVG = """SELECT
                                       MIN(cur_date), MAX(cur_date), SUM(games_played),
                                       SUM(goals), SUM(assists), SUM(winnings), SUM(defeats), SUM(draws),
                                       ROUND((CAST(SUM(goals) AS numeric) / CAST(SUM(games_played) AS numeric)), 2),
                                       ROUND((CAST(SUM(assists) AS numeric) / CAST(SUM(games_played) AS numeric)), 2),
                                       ROUND((CAST(SUM(winnings) AS numeric) / CAST(SUM(games_played) AS numeric)), 2),
                                       ROUND((CAST(SUM(defeats) AS numeric) / CAST(SUM(games_played) AS numeric)), 2),
                                       ROUND((CAST(SUM(draws) AS numeric) / CAST(SUM(games_played) AS numeric)), 2)
                                 FROM team_stats;"""

SELECT_GAMES_PLAYED_FROM_TEAM_STATS_TODAY = """SELECT games_played FROM team_stats
                                                    WHERE cur_date = CURRENT_DATE;"""

SELECT_GAMES_PLAYED_FROM_TEAM_STATS_ALL_TIME = """SELECT SUM(games_played) FROM team_stats"""
