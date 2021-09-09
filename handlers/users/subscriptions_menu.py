from aiogram import types
from aiogram.types.user import User
from utils.db_api.sqlighter import SQL

from loader import dp
import logging
from data import config

@dp.callback_query_handler(text_contains='subscriptions:team_subs')
async def show_team_subs(call: types.CallbackQuery):

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    message_user = User.get_current()['id']
    rq = SQL.get_team_subs(message_user)
    print(len(rq))
    if len(rq) == 0:
        await call.message.answer(text="Вы не подписанны ни на одну команду.")
    else:
        await call.message.answer(text="Вы подписанны на следующие команды:")
        for row in rq:
            await call.message.answer(text="👉 " + row[0])


@dp.callback_query_handler(text_contains='subscriptions:event_subs')
async def show_event_subs(call: types.CallbackQuery):

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    message_user = User.get_current()['id']
    rq = SQL.get_event_subs(message_user)
    print(len(rq))
    if len(rq) == 0:
        await call.message.answer(text="Вы не подписанны ни на один конкурс.")
    else:
        await call.message.answer(text="Вы подписанны на следующие конкурсы:")
        for row in rq:
            await call.message.answer(text="👉 " + row[0])
