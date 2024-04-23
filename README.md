# Flight Notification System

This repository contains a set of Python scripts for managing flight notifications, searching for flights, and managing flight data. These scripts are designed to work together to provide a comprehensive flight notification system.

## Requirements

To use this system, you'll need the following:

- Python 3.x
- Twilio account for SMS notifications
- Kiwi API key for flight searches
- Sheety API for managing flight data
- dotenv Python package for managing environment variables

## Setup

1. Clone this repository to your local machine.
```bash
git clone https://github.com/Pawlik-Lukasz/Travelling_project
```
2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```
Set up your environment variables:
Create a .env file in the root directory of the project and add the following variables:

```
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE=your_twilio_phone_number
CLIENT_PHONE=recipient_phone_number
SEARCH_API=your_kiwi_api_key
SHEETY_API=your_sheety_api_endpoint
SHEETY_AUTH=your_sheety_auth_token
```
Replace the placeholder values with your actual credentials.

## Contributing

Feel free to contribute to this project by opening issues or pull requests.

## Modifications

Some aspects can be added or modified,
for example running this project in real time or changing sheety to SQL database.

