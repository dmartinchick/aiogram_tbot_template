# TODO: Переименовать файл. он должен формировать не только клавиатуру для team

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.callback_datas import subscriptions_manager_choice

def make_callback_data(type_subs, item_name):
    return subscriptions_manager_choice.new(type_subs=type_subs, item_name=item_name)

#TODO: реализовать многоуровневость
async def get_items_kb(items_list, subscribe):

    print("enter in get_items_kb")
    #Создаем клавиатуру
    inkb_subs = InlineKeyboardMarkup(row_width=2)
    print("create_inkb_subs")
    # Проходимся по каждому элементу списка и создаем кнопки
    for item in items_list:

        button_text = item['name']

        # TODO: облогородить калбэки. 
        callback_data = make_callback_data(subscribe, item['id'])

        inkb_subs.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return inkb_subs
