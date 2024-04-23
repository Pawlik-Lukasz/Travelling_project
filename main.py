import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import dictionary_flight_data

manager = DataManager()
sheet_data = manager.get_data()
Flight_Search = FlightSearch()
Sms_Sender = NotificationManager()

for line in sheet_data:
    # search cheap flights via flight_search
    flights = Flight_Search.search_flight(dictionary_flight_data["departure_city"], line["iataCode"],
                                          dictionary_flight_data["tomorrow"], dictionary_flight_data["six_months"],
                                          dictionary_flight_data["seven_days"],
                                          dictionary_flight_data["twentyeight_days"],
                                          dictionary_flight_data["currency"], dictionary_flight_data["stopovers"],
                                          dictionary_flight_data["one_for_city"], line["lowestPrice"])
    # send text messages for cheap flights
    for connection in flights["data"]:
        Sms_Sender.send_sms(connection['price'], dictionary_flight_data["currency"], connection["cityFrom"],
                            connection["cityCodeFrom"], connection['cityTo'], connection["cityCodeTo"],
                            datetime.datetime.fromtimestamp(connection["route"][0]["dTime"]).strftime("%d-%m-%Y"),
                            datetime.datetime.fromtimestamp(connection["route"][1]["dTime"]).strftime("%d-%m-%Y"))
