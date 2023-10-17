import requests
from decouple import config
from datetime import datetime, timedelta

TODAY = datetime.now()
TOMORROW = TODAY + timedelta(days=1)
FLIGHT_FROM = "SAO"

TEQUILA_KEY = config("TEQUILA_KEY")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"


header = {
    "apikey": TEQUILA_KEY
}


class FlightSearch:
    def __init__(self, flight_to, max_price) -> None:
        self.flight_to = flight_to
        self.max_price = max_price

    def flight_search(self):
        parameters = {
            "fly_from": FLIGHT_FROM,
            "fly_to": self.flight_to,
            "date_from": TOMORROW.strftime("%d/%m/%Y"),
            "date_to": (TOMORROW + timedelta(days=6*30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "BRL",
            "price_to": self.max_price,
            "max_stopovers": 0,
        }
        f_search = requests.get(
            url=f"{TEQUILA_ENDPOINT}/search", headers=header, params=parameters)
        return f_search.json()
