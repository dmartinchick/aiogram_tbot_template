from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import contests_menu_choice


inkb_contests_menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Техника пешеходного туризма",callback_data=contests_menu_choice.new(
                item_name = "hiking_technique"
            )),
        ],
        [
            InlineKeyboardButton(text="Ловкость рук",callback_data="contests:sleight_of_hand")
        ],
        [
            InlineKeyboardButton(text="Борьба за мужика",callback_data="contests:fight_for_the_man")
        ],
        [
            InlineKeyboardButton(text="Боди-арт" ,callback_data="contests:body_art")
        ],
        [
            InlineKeyboardButton(text="Ночное ориентирование" ,callback_data="contests:night_orientation")
        ],
        [
            InlineKeyboardButton(text="Велотуризм", callback_data="contests:cycling_tourism")
        ],
        [
            InlineKeyboardButton(text="Волейбол", callback_data="contests:volleyball")
        ],
        [
            InlineKeyboardButton(text="Молот Тора", callback_data="contests:thors_hammer")
        ],
        [
            InlineKeyboardButton(text="Выбивалы", callback_data="contests:knockers")
        ],
        [
            InlineKeyboardButton(text="Бивуак", callback_data="contests:bivouac")
        ],
        [
            InlineKeyboardButton(text="Драник-fest", callback_data="contests:dranik-fest")
        ],
        [
            InlineKeyboardButton(text="Творческий конкурс", callback_data="contests:creative_competition")
        ],
        [
            InlineKeyboardButton(text="Туристический маршрут", callback_data="contests:tourist_route")
        ],
        [
            InlineKeyboardButton(text="Перетягивание каната", callback_data="contests:tug_of_war")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="contests:back")
        ]
    ]
)
