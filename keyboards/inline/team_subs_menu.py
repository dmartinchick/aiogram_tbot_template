from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import team_subs_menu


inkb_team_subs_menu = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        InlineKeyboardButton(text="Подписаться", callback_data=team_subs_menu)
    ]
)