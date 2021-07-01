from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import result_menu_choice

inkb_result_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Кубок фестиваля", callback_data=result_menu_choice.new(
                item_name = "festival"
            )),
        ],
        [
            InlineKeyboardButton(text="Кубок холдинга", callback_data="result:holding"),
        ],
        [
            InlineKeyboardButton(text="Кубок туризма", callback_data="result:tourism"),
        ],
        [
            InlineKeyboardButton(text="Кубок спорта", callback_data="result:sport"),
        ],
        [
            InlineKeyboardButton(text="Кубок культуры", callback_data="result:culture"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="result:back"),
        ],
    ]
)