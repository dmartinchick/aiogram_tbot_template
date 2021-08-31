from asyncio.windows_events import NULL
from aiogram import types
#from aiogram.types.callback_query import CallbackQuery
#from aiogram.types.message import Message
#from aiogram.dispatcher.filters import Command

from datetime import datetime, timedelta

from aiogram.types.user import User

from utils.db_api.sqlighter import SQL

#Загрузка клавиатур
from keyboards.inline.inline_main_menu import inkb_main_menu
from keyboards.inline.result_menu import inkb_result_menu
from keyboards.inline.contests_menu import inkb_contests_menu
from keyboards.inline.subscriptions_menu import inkb_subscriptions_menu

from loader import dp
import logging
from data import config

@dp.message_handler(commands=['Меню', 'menu'], commands_prefix = ['⠀','/'])
async def show_main_menu(message: types.Message):
    await message.answer(text="Главное меню", reply_markup=inkb_main_menu)


@dp.callback_query_handler(text_contains='back')
async def back_main_menu(call: types.CallbackQuery):
    """Возвращает пользователя в главное меню
    """
    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(text="Главное меню", reply_markup=inkb_main_menu)

@dp.callback_query_handler(text_contains="main:what_now")
async def show_what_now(call: types.CallbackQuery):
    """Возвращает пользователю текущее событие
    """

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    # текущее время и дата
    # TODO: заменить tdate
    # tdate = datetime.now() + timedelta(hours=config.DELTA)
    tdate = datetime(2021, 7, 18, 19, 29) + timedelta(hours=config.DELTA)
    dt_start = SQL.get_date_start()
    dt_end = SQL.get_date_end()

    # Проверка начался ли фестиваль
    if tdate < dt_start:
        await call.message.answer("😁 Фестиваль еще не начался, \nЗагляни сюда 18 июня!")
    elif tdate > dt_end:
        await call.message.answer("☹ К сожелению, фестиваль уже прошел.\nУвидимся в следующем году! 😁")
    else:
        await call.message.answer(text='🤓 Сейча проходит 🤓')
        
        # обращение к базе данных и получение данных
        rq = SQL.what_now_db(tdate)
       
        # запуск цикла обработки текущих событий
        for event in rq:
            # парсинг данных
            event_name = event[0]
            # time_start = event[1].strftime('%d.%m %H:%M')
            # time_end = event[2].strftime('%d.%m %H:%M')
            # address = event[3]
            # contains = event[4]

            # отправка сообщения с информацией о конкурсе
            await call.message.answer(event_name)


@dp.callback_query_handler(text_contains="main:what_next")
async def show_what_next(call: types.CallbackQuery):
    """Возвращает пользователю ближайшее событие
    """
    #TODO: реализовать функцию show_what_next. добавить обратный отсчет?

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    # получение текущей даты и времени, а так же даты и времени окончания фестиваля
    # TODO: заменить tdate
    # tdate = datetime.now() + timedelta(hours=config.DELTA)
    tdate = datetime(2021, 7, 18, 19, 29) + timedelta(hours=config.DELTA)
    dt_end = SQL.get_date_end()
    # проверка не закончился ли фестиваль
    if tdate >= dt_end:
        await call.message.answer("☹ К сожелению, фестиваль уже прошел.\nУвидимся в следующем году! 😁")
    else:
        # обращение к БД и получение ближайших мероприятий
        rq = SQL.what_next_db(tdate)

        # запуск цикла обработки текущих событий
        for event in rq:
            # парсинг данных
            event_name = event[0]
            time_start = event[1].strftime('%d.%m %H:%M')
            # time_end = event[2].strftime('%d.%m %H:%M')
            # address = event[3]
            # contains = event[4]
            await call.message.answer(f"{event_name}\nНачало: {time_start}")


@dp.callback_query_handler(text_contains="main:full_schedule")
async def show_full_schedule(call: types.CallbackQuery):
    """Возвращает пользователю полное расписание
    """
    #TODO: реализовать функцию show_full_schedule

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Вот полное расписание")
    pass


@dp.callback_query_handler(text_contains="main:results")
async def show_results_menu(call: types.CallbackQuery):
    """Возвращает пользователю таблицы результатов
    """

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Выбери интересующие тебя результаты", reply_markup=inkb_result_menu)


@dp.callback_query_handler(text_contains="main:contests")
async def show_contests_menu(call: types.CallbackQuery):
    """Возвращает пользователю меню конкурсов
    """

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    
    await call.message.answer("Выбирите интересующий вас конкурс", reply_markup=inkb_contests_menu)
    pass


@dp.callback_query_handler(text_contains="main:subscriptions")
async def show_subscriptions_menu(call: types.CallbackQuery):
    """Возвращает пользователю меню подписок
    """
    #TODO: реализовать функцию show_subscriptions_menu

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    message_user = User.get_current()['id']
    rq = SQL.get_users_subs(message_user)
    if rq == []:
        await call.message.answer(text="К сожелению, у вас нет подписок, хотите подписаться?",reply_markup=inkb_subscriptions_menu)
    else:
        await call.message.answer(text="Вы подписанны на:")
        await call.message.answer(rq)
        await call.message.answer(text="Менеджер подписок",reply_markup=inkb_subscriptions_menu)


@dp.callback_query_handler(text_contains="main:map")
async def show_map(call: types.CallbackQuery):
    """Возвращает пользователю кеарту фестиваля
    """
    #TODO: реализовать функцию show_map

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Вот карта фестиваля")
    pass


@dp.callback_query_handler(text_contains="main:share")
async def show_share(call: types.CallbackQuery):
    """Возвращает пользователю QR-код со сылкой на этот телеграм бот
    """
    #TODO: реализовать функцию show_share

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Вот ссылка на телеграмм бота")
    pass


@dp.callback_query_handler(text_contains="main:about")
async def show_about(call: types.CallbackQuery):
    """Возвращает пользователю документ с положением фестиваля
    """
    #TODO: реализовать функцию show_about

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Положение туристического фестиваля Свароог2022")
    pass
