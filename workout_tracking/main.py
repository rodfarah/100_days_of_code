from decouple import config
import requests as rq

NUTRIXIONIX_KEY = config("NUTRIXIONIX_KEY")
NUTRIXIONIX_ID = config("NUTRIXIONIX_ID")
NUTRIXIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


AGE = 47
WEIGHT = 75
HEIGHT = 181
GENDER = "male"

exercise = input("Tell me about the exercise you practiced: ")

headers = {
    "x-app-id" : NUTRIXIONIX_ID,
    "x-app-key" : NUTRIXIONIX_KEY
}


main_data = {
    "query" : exercise,
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE
}

request = rq.post(url= NUTRIXIONIX_ENDPOINT, json=main_data, headers=headers)

print(request.text)