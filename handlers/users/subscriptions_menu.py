from aiogram import types
from aiogram.types.user import User
from utils.db_api.sqlighter import SQL

from loader import dp
import logging
from data import config
from utils.misc.other import get_unsubs_list

from keyboards.inline.subs_team import get_items_kb



@dp.callback_query_handler(text_contains='subscriptions:team_subs')
async def show_team_subs(call: types.CallbackQuery):

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Получение Id пользователя
    message_user = User.get_current()['id']
    
    # получаем полный список команд
    teams_list = SQL.get_teams_all()
    # получаем список команд на которые подписан пользователь
    teams_subs_user = SQL.get_team_subs(message_user)
    # создаем список команд на которые может подписаться пользователь
    teams_unsubs_user = get_unsubs_list(teams_list, teams_subs_user)


    # Проверяем есть ли пользователя подписки
    if len(teams_subs_user) == 0:
        teams_subs_markup = get_items_kb(teams_unsubs_user, True) 
        await call.message.answer(text="Вы не подписаны ни на одну команду."
                                        "Вы можете подписаться на новости команды "
                                        "просто нажав на кнопку с её названием",
                                        reply_markup = teams_subs_markup)
    elif len(teams_unsubs_user) == 0:
        teams_unsubs_markup = get_items_kb(teams_list, False)
        await call.message.answer(text="Вы подписаны на все команды."
                                        "Вы можете отписаться от неинтересующей вас команды "
                                        "просто нажав на кнопку с её названием",
                                        reply_markup=teams_unsubs_markup)
    else:
        teams_subs_markup = get_items_kb(teams_unsubs_user, True)
        teams_unsubs_markup =get_items_kb(teams_list, False)
        await call.message.answer(text="Выподписаны на:", reply_markup=teams_unsubs_markup)
        await call.message.answer(text="Вы не подписаны на:", reply_markup=teams_unsubs_markup)


    #TODO: добавить инлайн кнопку "Добавить подписку" которая будет вести на полный списко команд.
    #TODO: добавить инлайн кнопку "Отменить подписку" которая будет вести на полный списко команд.

@dp.callback_query_handler(text_contains='subscriptions:event_subs')
async def show_event_subs(call: types.CallbackQuery):

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    message_user = User.get_current()['id']
    rq = SQL.get_event_subs(message_user)
    
    if len(rq) == 0:
        await call.message.answer(text="Вы не подписанны ни на один конкурс.")
    else:
        await call.message.answer(text="Вы подписанны на следующие конкурсы:")
        for row in rq:
            await call.message.answer(text="👉 " + row[0])
    #TODO: добавить инлайн кнопку "Добавить подписку" которая будет вести на полный списко конкурсов.
    #TODO: добавить инлайн кнопку "Отменить подписку" которая будет вести на полный списко конкурсов.