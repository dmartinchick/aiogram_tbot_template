from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data
from utils.db_api.sqlighter import SQL

from keyboards.inline.callback_datas import subscriptions_team_choice

#TODO: реализовать многоуровневость
async def get_teams_list(message_user):

    #Создаем клавиатуру
    inkb_subs_teams = InlineKeyboardMarkup(row_width=2)

    #TODO: Вынести в отдельную функцию. Возможно в отдельный файл вынести
    all_teams = SQL.get_teams_all()
    user_teams_subs = SQL.get_team_subs(message_user)
    user_teams_unsubs = []
    for team in all_teams:
        if team not in user_teams_subs:
            user_teams_unsubs.append(str(team[0]))

    for team in user_teams_unsubs:

        button_text = team

        # TODO: облогородить калбэки. 
        callback_data = "make_callback_data"

        inkb_subs_teams.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return inkb_subs_teams


