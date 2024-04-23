import os

import requests
import os
from dotenv import find_dotenv

dotenv_path = find_dotenv()


class DataManager:

    def __init__(self):
        self.sheety_data = {}
        self.sheety_API = os.getenv('SHEETY_API')
        self.sheety_AUTH = os.getenv('SHEETY_AUTH')

    def get_data(self):
        headers = {
            "Authorization": "Bearer " + self.sheety_AUTH
        }
        sheety_response = requests.get(url=self.sheety_API, headers=headers)

        self.sheety_data = sheety_response.json()["flightProject"]
        return self.sheety_data

    def put_data(self):
        for line in self.sheety_data:
            id = line["id"]
            headers = {
                "Authorization": "Bearer " + self.sheety_AUTH
            }
            body = {
                "flightProject": {
                    "iataCode": line["iataCode"]
                }
            }
            sheety_put_API = f"{self.sheety_API}/{id}"
            sheety_put_response = requests.put(url=sheety_put_API, json=body, headers=headers)
            print("response.text= ", sheety_put_response.text)
