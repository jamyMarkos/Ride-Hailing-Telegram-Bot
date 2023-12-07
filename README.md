# Ride Share Telegram Bot

This Telegram bot facilitates ride sharing by allowing users to sign up, log in, manage their profiles, and request rides.

## Features

- **User Authentication:**
  - Sign up and log in using Telegram accounts.
  - Provide full name, phone number, and role (driver/passenger).
  - Utilize the share phone number feature for receiving phone numbers.

- **Profile Management:**
  - Edit profiles with details such as name and contact information.
  - Use commands like `/edit_name`, `/edit_phone`, `/edit_role` for editing.

- **Ride Booking:**
  - Request rides by providing current location and destination.
  - Receive estimated arrival times and fare estimates.

## Folder Structure

```plaintext
ride_share_bot/
│
├── bot/
│   ├── __init__.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── authentication.py
│   │   ├── profile.py
│   │   ├── ride.py
│   │   └── ...
│   │
│   ├── states.py
│   ├── main.py
│   └── settings.py
│
├── venv/
│
├── .gitignore
└── requirements.txt
