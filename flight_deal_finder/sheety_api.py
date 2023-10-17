import requests as rq
from decouple import config

SHEETY_USERNAME = config("SHEETY_USERNAME")
SHEETY_KEY = config("SHEETY_KEY")
SHEETY_PROJECT_NAME = config("SHEETY_PROJECT_NAME")
SHEETY_SHEET_NAME = config("SHEETY_SHEET_NAME")

SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

header = {
    "Authorization": f"Bearer {SHEETY_KEY}",
}


class SheetRequest:
    def get_all_data(self):
        request = rq.get(url=SHEETY_ENDPOINT, headers=header)
        return request


sheet = SheetRequest()

print(sheet.get_all_data())
