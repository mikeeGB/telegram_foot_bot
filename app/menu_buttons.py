from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Main MENU
btn_write_goals = KeyboardButton('⚽ Записать голы')
btn_write_assists = KeyboardButton('🅰️ Записать ассисты')
btn_show_stats = KeyboardButton('🔝 Показать статистику')
btn_end_match_day = KeyboardButton('✅ Завершить игровой день')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_write_goals, btn_write_assists,
                                                          btn_show_stats, btn_end_match_day)


# Sub Menu Goals
btn_1_goal = KeyboardButton('1 Goal: ⚽')
btn_2_goal = KeyboardButton('2 Goals: ⚽⚽')
btn_3_goal = KeyboardButton('3 Goals: ⚽⚽⚽')
btn_4_goal = KeyboardButton('4 Goals: ⚽⚽⚽⚽')
btn_5_goal = KeyboardButton('5 Goals: ⚽⚽⚽⚽⚽')

sub_menu_goals = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_1_goal, btn_2_goal,
                                                               btn_3_goal, btn_4_goal,
                                                               btn_5_goal)

# sub menu asking goals
btn_finish_writing_g = KeyboardButton('Завершить матч')
btn_continue_writing_goals_1 = KeyboardButton('Записать еще голы')
btn_continue_writing_assists_1 = KeyboardButton('Записать ассисты')

sub_menu_goals_writing = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_continue_writing_goals_1,
                                                                       btn_continue_writing_assists_1,
                                                                       btn_finish_writing_g)


# Sub Menu Assists
btn_1_assist = KeyboardButton('1 Assist: 🎯')
btn_2_assist = KeyboardButton('2 Assists: 🎯🎯')
btn_3_assist = KeyboardButton('3 Assists: 🎯🎯🎯')
btn_4_assist = KeyboardButton('4 Assists: 🎯🎯🎯🎯')
btn_5_assist = KeyboardButton('5 Assists: 🎯🎯🎯🎯🎯')

sub_menu_assists = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_1_assist, btn_2_assist,
                                                                 btn_3_assist, btn_4_assist,
                                                                 btn_5_assist)

# sub menu asking assists
btn_finish_writing_assists = KeyboardButton('Завершить матч')
btn_continue_writing_assists_2 = KeyboardButton('Записать еще ассисты')
btn_continue_writing_goals_2 = KeyboardButton('Записать голы')

sub_menu_assists_writing = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_continue_writing_assists_2,
                                                                         btn_continue_writing_goals_2,
                                                                         btn_finish_writing_assists)
