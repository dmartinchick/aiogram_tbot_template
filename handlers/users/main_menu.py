from aiogram import types
from aiogram.types.callback_query import CallbackQuery
from aiogram.types.message import Message
from aiogram.dispatcher.filters import Command

#Загрузка клавиатур
from keyboards.inline.inline_main_menu import inkb_main_menu

from loader import dp
import logging

@dp.message_handler(commands=['Меню', 'menu'], commands_prefix = ['⠀','/'])
async def show_main_menu(message: types.Message):
    await message.answer(text="Главное меню", reply_markup=inkb_main_menu)

@dp.callback_query_handler(text_contains="main:what_now")
async def show_what_now(call: types.CallbackQuery):
    """Возвращает пользователю текущее событие
    """
    #TODO: реализовать функцию show_what_now

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    

    await call.message.answer("Ты только глянь, что сейчас происходит")
    pass


@dp.callback_query_handler(text_contains="main:what_next")
async def show_what_next(call: types.CallbackQuery):
    """Возвращает пользователю ближайшее событие
    """
    #TODO: реализовать функцию show_what_next. добавить обратный отсчет?

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Ты только глянь, что скоро начнеться")
    pass


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
    #TODO: реализовать функцию show_results_menu

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Вот результаты")
    pass


@dp.callback_query_handler(text_contains="main:contests")
async def show_contests_menu(call: types.CallbackQuery):
    """Возвращает пользователю меню конкурсов
    """
    #TODO: реализовать функцию show_contests_menu

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Вот конкурсы")
    pass


@dp.callback_query_handler(text_contains="main:subscriptions")
async def show_subscriptions_menu(call: types.CallbackQuery):
    """Возвращает пользователю меню подписок
    """
    #TODO: реализовать функцию show_subscriptions_menu

    await call.answer(cache_time=360)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    
    await call.message.answer("Вот менеджер пописок")
    pass


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
