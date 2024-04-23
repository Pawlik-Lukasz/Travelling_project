from twilio.rest import Client
import os
from dotenv import find_dotenv

dotenv_path = find_dotenv()


class NotificationManager:

    def __init__(self):
        # sid and token for TWILIO
        self.account_sid = os.getenv('ACCOUNT_SID')
        self.auth_token = os.getenv('AUTH_TOKEN')

    def send_sms(self, price, currency, departure_city_name, departure_city_code, arrival_city_name, arrival_city_code,
                 go_date, back_date):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
            body=f"Wow, you have an occasion to buy cheap flight! Only {price} {currency} for fly from "
                 f"{departure_city_name}-{departure_city_code} to {arrival_city_name}-{arrival_city_code} in date {go_date} - {back_date}",
            from_=os.getenv('TWILIO_PHONE'),
            to=os.getenv('CLIENT_PHONE')
        )
        print(message)
        return message
