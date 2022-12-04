import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from main import dp

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    keyboard_list = [
        [types.KeyboardButton('Profile'), types.KeyboardButton(text='Document wizard')],
        [types.KeyboardButton('Search'), types.KeyboardButton('Support')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard_list)

    await message.reply("Welcome to the Menu!", reply=False)
    await message.reply("Choose the button:", reply_markup=keyboard, reply=False)