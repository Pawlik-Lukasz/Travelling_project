import datetime

today = datetime.datetime.now()
tomorrow = (today + datetime.timedelta(1, 0)).strftime("%d/%m/%Y")
six_months = (today + datetime.timedelta(30 * 6, 0)).strftime("%d/%m/%Y")
seven_days = (today + datetime.timedelta(7, 0)).strftime("%d/%m/%Y")
twentyeight_days = (today + datetime.timedelta(28, 0)).strftime("%d/%m/%Y")

dictionary_flight_data = {
    "departure_city": "WAW",
    "currency": "PLN",
    "stopovers": 0,
    "one_for_city": 1,
    "tomorrow": tomorrow,
    "six_months": six_months,
    "seven_days": seven_days,
    "twentyeight_days": twentyeight_days


}
