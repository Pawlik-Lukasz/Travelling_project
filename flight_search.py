import requests
import os
from dotenv import find_dotenv

dotenv_path = find_dotenv()


class FlightSearch:
    def __init__(self):
        # Include Your API key from Kiwi page
        self.search_API = os.getenv('SEARCH_API')
        self.iata_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.search_endpoint = "https://tequila-api.kiwi.com/search"

    def city_names(self, city_name):
        headers = {
            "apikey": self.search_API
        }
        body = {
            "term": city_name,
            "location_types": "city"
        }
        search_response = requests.get(url=self.iata_endpoint, params=body, headers=headers)
        json_response = search_response.json()["locations"][0]["code"]

        return json_response

    def search_flight(self, fly_from, fly_to, date_from, date_to, return_from, return_to, curr, stopovers, cheapest,
                      price_to):
        headers = {
            "apikey": self.search_API
        }
        body = {
            "fly_from": f"city:{fly_from}",
            "fly_to": f"city:{fly_to}",
            "date_from": date_from,
            "date_to": date_to,
            "return_from": return_from,
            "return_to": return_to,
            "curr": curr,
            "max_stopovers": stopovers,
            "one_for_city": cheapest,
            "price_to": price_to,
            "flight_type": "round",

        }

        search_response = requests.get(url=self.search_endpoint, params=body, headers=headers)
        if search_response.json()["_results"] == 0:
            stopovers += 1
            search_response = requests.get(url=self.search_endpoint, params=body, headers=headers)
            print(search_response.json())
            stopovers -= 1

            return search_response.json()
        else:
            return search_response.json()
