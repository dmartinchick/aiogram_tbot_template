from aiogram import types
from datetime import datetime

from utils.db_api.sqlighter import SQL

from loader import dp
import logging
from data import config

@dp.callback_query_handler(text_contains="contests:hiking_technique")
async def show_hiking_technique_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о технике пешеходного туризма
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")


@dp.callback_query_handler(text_contains="contests:sleight_of_hand")
async def show_sleight_of_hand_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Ловкости рук
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:fight_for_the_man")
async def show_fight_for_the_man_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Борьбе за мужика
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:body_art")
async def show_body_art_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Боди-арте
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:night_orientation")
async def show_night_orientation_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Ночном ориентировании
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:cycling_tourism")
async def show_cycling_tourism_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Велотуризме
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:volleyball")
async def show_volleyball_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Волебойле
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:thors_hammer")
async def show_thors_hammer_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Молоте тора
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:knockers")
async def show_knockers_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Выбивалах
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:bivouac")
async def show_bivouac_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Бивуаке
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:dranik_fest")
async def show_dranik_fest_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Драник-фесте
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:creative_competition")
async def show_creative_competition_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Творческом конкурсе
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:tourist_route")
async def show_tourist_route_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Туристическом маршруте
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")



@dp.callback_query_handler(text_contains="contests:tug_of_war")
async def show_tug_of_war_info(call: types.CallbackQuery):
    """Возвращает пользователю информацию о Перетягивании каната
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    # Обращение к БД
    name_en = callback_data[9:]
    rq = SQL.contests_db(name_en)

    name = rq[0]
    type = rq[1]
    coefficient = rq[2]
    rule = rq[3]
    composition = rq[4]
    time_start = rq[5].strftime('%d.%m %H:%M')

    await call.message.answer(text=f"{name}\n"
                            f"{type}\n\n"
                            f"Коэффициент сложности:\n{coefficient}\n\n"
                            f"Состав участников:\n{composition}\n\n"
                            f"Дата и время начала:\n{time_start}\n\n"
                            f"Правила:\n{rule}")

