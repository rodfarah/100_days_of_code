import requests as rq
from twilio.rest import Client
from decouple import config

OWM_Endpoint = config("OWM_Endpoint")
API_KEY = config("API_KEY")
LATITUDE = -31.25
LONGITUDE = -55.2833
TWILIO_PHONE_NUM = config("SMS_FROM")

data_to_exclude = "current,minutely,daily"
weather_params = {"lat": LATITUDE,
                  "lon": LONGITUDE,
                  "exclude": data_to_exclude,
                  "appid": API_KEY}

response = rq.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

hourly_data = response.json()["hourly"]

for n in range(12):
    if hourly_data[n]["weather"][0]["id"] < 700:
        account_sid = config("SMS_SID")
        auth_token = config("SMS_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body="Today will be a rainy day, bring your umbrela!",
                from_=TWILIO_PHONE_NUM,
                to=config("SMS_TO")
            )
        print(message.status)
        break
