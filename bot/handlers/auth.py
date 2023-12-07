# authentication.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode

from . import dp  # Import the dispatcher instance from main module
from . states import AuthState

@dp.message_handler(Command("start"), state="*")
async def start(message: types.Message):
    # Start command initiates the authentication process
    await message.answer("Welcome to the ride share bot! Please provide the following information to sign up.")

    await AuthState.waiting_for_name.set()
    await message.answer("1. Your Full Name:")

@dp.message_handler(state=AuthState.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    # Process the user's full name
    full_name = message.text.strip()

    # Save the full name to the state
    await state.update_data(full_name=full_name)

    await AuthState.next()
    await message.answer("2. Your Phone Number:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(content_types=types.ContentType.CONTACT, state=AuthState.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    # Process the user's phone number
    phone_number = message.contact.phone_number

    # Save the phone number to the state
    await state.update_data(phone_number=phone_number)

    await AuthState.next()
    await message.answer("3. Your Role (Driver/Passenger):", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=AuthState.waiting_for_role)
async def process_role(message: types.Message, state: FSMContext):
    # Process the user's role (Driver/Passenger)
    role = message.text.strip().lower()

    # Validate the role
    if role not in ["driver", "passenger"]:
        await message.answer("Invalid role. Please enter 'Driver' or 'Passenger'.")
        return

    # Save the role to the state
    await state.update_data(role=role)

    # Registration is complete
    user_data = await state.get_data()
    full_name = user_data.get("full_name")
    phone_number = user_data.get("phone_number")
    role = user_data.get("role")

    # Here you can save the user data to your database or perform any other necessary actions

    await state.finish()
    await message.answer(f"Registration complete!\n\n"
                         f"Full Name: {full_name}\n"
                         f"Phone Number: {phone_number}\n"
                         f"Role: {role}",
                         parse_mode=ParseMode.MARKDOWN)
    
@dp.message_handler(Command("profile"), state="*")
async def profile_management(message: types.Message):
    await message.answer("You are currently in profile management mode. What would you like to edit?\n"
                         "1. /edit_name - Edit your full name\n"
                         "2. /edit_phone - Edit your phone number\n"
                         "3. /edit_role - Edit your role (Driver/Passenger)")


