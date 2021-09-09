from aiogram import types

from utils.db_api.sqlighter import SQL

from loader import dp
import logging
from data import config

@dp.callback_query_handler(text_contains='subscriptions:team_subs')
async def show_team_subs(call: types.CallbackQuery):

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(text="Вы подписанны на следующие команды:")


@dp.callback_query_handler(text_contains='subscriptions:event_subs')
async def show_event_subs(call: types.CallbackQuery):

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(text="Вы подписанны на следующие мероприятия:")
