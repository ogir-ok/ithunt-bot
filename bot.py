"""
This is a echo bot.
It echoes any incoming text messages.
"""
import os
import logging
import aiohttp
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('BOT_TOKEN')
WEB_URL = os.getenv('WEB_URL', 'http://web:9000')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


async def store_message(message):
    async with aiohttp.ClientSession() as session:
        await session.post(f'{WEB_URL}/api/v1/message/new/', data=f'{message.text}')


@dp.message_handler()
async def echo(message: types.Message):
    await store_message(message)
    await message.answer('ok')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

