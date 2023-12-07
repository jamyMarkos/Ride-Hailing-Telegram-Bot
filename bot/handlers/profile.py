# handlers/profile.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from .. import dp  # Import the dispatcher instance from main module
from ..states import ProfileState

@dp.message_handler(Command("edit_name"), state="*")
async def edit_name(message: types.Message):
    await message.answer("Please enter your new full name:")
    await ProfileState.waiting_for_new_name.set()

@dp.message_handler(state=ProfileState.waiting_for_new_name)
async def process_new_name(message: types.Message, state: FSMContext):
    new_name = message.text.strip()

    # Update the user's name in the database or any other action
    # For simplicity, we'll just echo the new name
    await message.answer(f"Your name has been updated to: {new_name}")

    await state.finish()

# Similar handlers for /edit_phone and /edit_role can be added here

# ... (other profile management commands)
