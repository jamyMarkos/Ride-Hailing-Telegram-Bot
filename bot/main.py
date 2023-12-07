# main.py

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram import Bot, Dispatcher, types
# from aiogram.dispatcher.middlewares.logging import LoggingMiddleware
import logging


logging.basicConfig(level=logging.INFO)



from bot import settings
from bot.states import AuthState, ProfileState  # Import ProfileState

bot = Bot(token=settings.TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Initialize states
dp.register_state(AuthState)
dp.register_state(ProfileState)  # Register ProfileState

# ... (other setup code)
