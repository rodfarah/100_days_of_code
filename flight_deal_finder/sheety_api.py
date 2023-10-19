import requests as rq
from decouple import config
from flight_api import FlightSearch

SHEETY_USERCODE = config("SHEETY_USERCODE")
SHEETY_TOKEN = config("SHEETY_TOKEN")
SHEETY_PROJECT_NAME = config("SHEETY_PROJECT_NAME")
SHEETY_SHEET_NAME = config("SHEETY_SHEET_NAME")

SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERCODE}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}


class SheetRequest:

    def get_all_data(self):
        request = rq.get(url=SHEETY_ENDPOINT, headers=header)
        return request.json()["prices"]

    def edit_row(self, row_num: int, new_content: dict):
        parameters = {
            "price": new_content
        }
        request = rq.put(url=f"{SHEETY_ENDPOINT}/{row_num}",
                         headers=header, json=parameters)
