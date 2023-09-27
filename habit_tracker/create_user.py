import requests as rq
from decouple import config

PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"

PIXELA_TOKEN = config("PIXELA_TOKEN")
PIXELA_USERNAME = config("PIXELA_USERNAME")

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = rq.post(url=PIXELA_USER_ENDPOINT, json= user_params)

print(response.text)
