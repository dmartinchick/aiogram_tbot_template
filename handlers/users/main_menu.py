from aiogram import types
from aiogram.types.message import Message
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(commands=['Меню', 'menu'], commands_prefix = ['⠀','/'])
async def show_main_menu(message: types.Message):
    await message.answer(text="Главное меню")