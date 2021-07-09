from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Main MENU
btn_write_goals = KeyboardButton('⚽ Записать голы')
btn_write_assists = KeyboardButton('🅰️ Записать ассисты')
btn_show_stats = KeyboardButton('🔝 Показать статистику')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_write_goals, btn_write_assists).add(btn_show_stats)


# Sub Menu Goals
btn_1_goal = KeyboardButton('1 Goal: ⚽')
btn_2_goal = KeyboardButton('2 Goals: ⚽⚽')
btn_3_goal = KeyboardButton('3 Goals: ⚽⚽⚽')
btn_4_goal = KeyboardButton('4 Goals: ⚽⚽⚽⚽')
btn_5_goal = KeyboardButton('5 Goals: ⚽⚽⚽⚽⚽')
btn_6_goal_menu = KeyboardButton('↩️Вернуться в меню')

sub_menu_goals = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_1_goal, btn_2_goal,
                                                               btn_3_goal, btn_4_goal,
                                                               btn_5_goal, btn_6_goal_menu)

# sub menu asking goals
btn_finish_writing_g = KeyboardButton('Завершить матч')
btn_continue_writing_goals_1 = KeyboardButton('Записать еще голы')
btn_continue_writing_assists_1 = KeyboardButton('Записать ассисты')

sub_menu_goals_writing = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_continue_writing_goals_1,
                                                                       btn_continue_writing_assists_1).add(
                                                                       btn_finish_writing_g)


# Sub Menu Assists
btn_1_assist = KeyboardButton('1 Assist: 🎯')
btn_2_assist = KeyboardButton('2 Assists: 🎯🎯')
btn_3_assist = KeyboardButton('3 Assists: 🎯🎯🎯')
btn_4_assist = KeyboardButton('4 Assists: 🎯🎯🎯🎯')
btn_5_assist = KeyboardButton('5 Assists: 🎯🎯🎯🎯🎯')
btn_6_assist_menu = KeyboardButton('↩️Вернуться в меню')


sub_menu_assists = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_1_assist, btn_2_assist,
                                                                 btn_3_assist, btn_4_assist,
                                                                 btn_5_assist, btn_6_assist_menu)

# sub menu asking assists
btn_finish_writing_assists = KeyboardButton('Завершить матч')
btn_continue_writing_assists_2 = KeyboardButton('Записать еще ассисты')
btn_continue_writing_goals_2 = KeyboardButton('Записать голы')

sub_menu_assists_writing = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_continue_writing_assists_2,
                                                                         btn_continue_writing_goals_2).add(
                                                                         btn_finish_writing_assists)


# sub menu asking winning/defeat/draw
btn_winning = KeyboardButton('👊 Победа')
btn_defeat = KeyboardButton('🤬 Поражение')
btn_draw = KeyboardButton('🤝 Ничья')

sub_menu_winning_defeat_draw = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_winning,
                                                                             btn_defeat).add(
                                                                             btn_draw)

# sub menu statistics
btn_individual_stats = KeyboardButton('🏋️‍♂ Индивидуальная статистика')
btn_team_stats = KeyboardButton('🏆 Командная статистика')
btn_stats_return = KeyboardButton('↩️Вернуться в меню')


sub_menu_stats = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_individual_stats).add(
                                                               btn_team_stats).add(
                                                               btn_stats_return)

# sub menu individual stats
btn_individual_stats_today = KeyboardButton('📅 Моя статистика за сегодня')
btn_individual_stats_all_time = KeyboardButton('🕐 Моя статистика за все время')
btn_ind_stats_return = KeyboardButton('↩️Меню выбора статистики')


sub_menu_individual_stats = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_individual_stats_today).add(
                                                                          btn_individual_stats_all_time).add(
                                                                           btn_ind_stats_return)

# sub menu team stats
btn_team_stats_today = KeyboardButton('🍅 Командная статистика за сегодня')
btn_team_stats_all_time = KeyboardButton('🥒 Командная статистика за все время')
btn_team_stats_return = KeyboardButton('↩️Меню выбора статистики')


sub_menu_team_stats = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_team_stats_today).add(
                                                                          btn_team_stats_all_time).add(
                                                                           btn_team_stats_return)
