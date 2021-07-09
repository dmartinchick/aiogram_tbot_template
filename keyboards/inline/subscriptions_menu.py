from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import subscriptions_menu_choice


inkb_subscriptions_menu = InlineKeyboardMarkup(
    inline_keyboard=(
        [
            InlineKeyboardButton(text="Подписки на команды",callback_data=subscriptions_menu_choice.new(
                item_name="team_subs"
            )),
        ],
        [
            InlineKeyboardButton(text="Подписки на конкурсы", callback_data="subscriptions:event_subs"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="subscription:back")
        ]
    )
)