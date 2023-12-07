# states.py

from aiogram.dispatcher.filters.state import State, StatesGroup

class AuthState(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_role = State()

class ProfileState(StatesGroup):
    waiting_for_new_name = State()
    waiting_for_new_phone = State()
    waiting_for_new_role = State()

class RideState(StatesGroup):
    waiting_for_current_location = State()
    waiting_for_destination = State()