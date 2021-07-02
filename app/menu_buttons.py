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

# sub menu asking
btn_finish_writing = KeyboardButton('Завершить матч')
btn_continue_writing = KeyboardButton('Записать еще голы')

sub_menu_goals_writing = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_finish_writing, btn_continue_writing)
