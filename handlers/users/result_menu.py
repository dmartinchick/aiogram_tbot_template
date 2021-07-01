from aiogram import types

from utils.db_api.sqlighter import SQL

from loader import dp
import logging
from data import config

@dp.callback_query_handler(text_contains='result:festival')
async def show_festival_result(call: types.CallbackQuery):
    """Возвращает пользователю таблицу результатов Кубка фестиваля
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(text="Таблица результатов Кубка фестиваля")


@dp.callback_query_handler(text_contains='result:holding')
async def show_holding_result(call: types.CallbackQuery):
    """Возвращает пользователю таблицу результатов Кубка холдинга
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(text="Таблица результатов Кубка холдинга")


@dp.callback_query_handler(text_contains='result:tourism')
async def show_tourism_result(call: types.CallbackQuery):
    """Возвращает пользователю таблицу результатов Кубка туризма
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(text="Таблица результатов Кубка туризма")


@dp.callback_query_handler(text_contains='result:sport')
async def show_sport_result(call: types.CallbackQuery):
    """Возвращает пользователю таблицу результатов Кубка спорта
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(text="Таблица результатов Кубка спорта")


@dp.callback_query_handler(text_contains='result:culture')
async def show_culture_result(call: types.CallbackQuery):
    """Возвращает пользователю таблицу результатов Кубка культуры
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(text="Таблица результатов Кубка культуры")
