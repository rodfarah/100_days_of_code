import requests
from decouple import config
from datetime import datetime, timedelta

TODAY = datetime.now()
TOMORROW = TODAY + timedelta(days=1)
FLIGHT_FROM = "SAO"

TEQUILA_KEY = config("TEQUILA_KEY")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"


header = {
    "apikey": TEQUILA_KEY
}


class FlightSearch:
    def __init__(self, flight_to_city: str) -> None:
        self.flight_to_city = flight_to_city

    def flight_search(self, to_airport_iata, max_price: float):
        self.max_price = max_price
        parameters = {
            "fly_from": FLIGHT_FROM,
            "fly_to": to_airport_iata,
            "date_from": TOMORROW.strftime("%d/%m/%Y"),
            "date_to": (TOMORROW + timedelta(days=6*30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "BRL",
            "price_to": self.max_price,
            "max_stopovers": 0,
        }
        f_search = requests.get(
            url=f"{TEQUILA_ENDPOINT}v2/search", headers=header, params=parameters)
        return f_search.json()

    def search_city_iata(self):
        parameters = {
            "term": self.flight_to_city,
            "location_types": "city",
            "locale": "en-US"
        }
        iata_search = requests.get(
            url=f"{TEQUILA_ENDPOINT}locations/query", headers=header, params=parameters)
        result = iata_search.json()
        return result["locations"][0]["code"]
