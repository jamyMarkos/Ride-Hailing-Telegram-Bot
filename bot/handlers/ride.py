# handlers/ride.py

import random
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode

from .. import dp  # Import the dispatcher instance from the main module
from ..states import RideState

# Initial ride booking functionality
@dp.message_handler(Command("request_ride"), state="*")
async def request_ride(message: types.Message):
    await message.answer("Let's get started with your ride request!\n"
                         "Please provide your current location:")

    await RideState.waiting_for_current_location.set()

@dp.message_handler(state=RideState.waiting_for_current_location)
async def process_current_location(message: types.Message, state: FSMContext):
    current_location = message.text.strip()

    # Save the current location to the state
    await state.update_data(current_location=current_location)

    await RideState.next()
    await message.answer("Great! Now, please provide your destination:")

@dp.message_handler(state=RideState.waiting_for_destination)
async def process_destination(message: types.Message, state: FSMContext):
    destination = message.text.strip()

    # Save the destination to the state
    await state.update_data(destination=destination)

    # Calculate estimated arrival time and fare (using random numbers for demonstration)
    estimated_arrival_time = random.randint(5, 15)  # Random number between 5 and 15 minutes
    estimated_fare = random.randint(10, 30)  # Random number between 10 and 30 dollars

    # Display estimated arrival time and fare to the user
    await message.answer(f"Estimated Arrival Time: {estimated_arrival_time} minutes\n"
                         f"Estimated Fare: ${estimated_fare}")

    # Reset the state
    await state.finish()

# New features: Rating and Reviews, History, and Receipts
@dp.message_handler(Command("rate_ride"), state="*")
async def rate_ride(message: types.Message):
    await message.answer("Please rate your ride experience from 1 to 5 (5 being the best):")
    await RideState.waiting_for_ride_rating.set()

@dp.message_handler(state=RideState.waiting_for_ride_rating)
async def process_ride_rating(message: types.Message, state: FSMContext):
    try:
        rating = int(message.text.strip())
        if 1 <= rating <= 5:
            # Save the rating to the database or any other action
            await message.answer(f"Thank you for your feedback! You rated the ride as {rating}.")
        else:
            await message.answer("Invalid rating. Please provide a rating between 1 and 5.")
    except ValueError:
        await message.answer("Invalid input. Please provide a numerical rating.")

    await state.finish()

@dp.message_handler(Command("ride_history"), state="*")
async def ride_history(message: types.Message):
    # Retrieve ride history from the database or any other action
    # For simplicity, let's assume a list of rides
    ride_history = ["Ride 1", "Ride 2", "Ride 3"]

    if ride_history:
        history_text = "\n".join(ride_history)
        await message.answer(f"Your ride history:\n{history_text}")
    else:
        await message.answer("You have no ride history.")

@dp.message_handler(Command("digital_receipt"), state="*")
async def digital_receipt(message: types.Message):
    # Generate a digital receipt for the latest completed ride
    # Retrieve the latest completed ride details from the database or any other action
    # For simplicity, let's assume ride details
    ride_details = {"driver": "Driver Name", "fare": "$20", "timestamp": "2023-12-10 15:30:00"}

    receipt_text = (
        f"Digital Receipt\n"
        f"Driver: {ride_details['driver']}\n"
        f"Fare: {ride_details['fare']}\n"
        f"Timestamp: {ride_details['timestamp']}"
    )

    await message.answer(receipt_text)
