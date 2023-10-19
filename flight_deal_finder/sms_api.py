from decouple import config
from twilio.rest import Client

# SMS Data
SMS_SID = config("SMS_SID")
SMS_TOKEN = config("SMS_TOKEN")
SMS_FROM = config("SMS_FROM")
SMS_TO = config("SMS_TO")

client = Client(SMS_SID, SMS_TOKEN)


def send_sms(cheapest_flights: list):
    text_under_construction = "Low price alert! "
    for flight in cheapest_flights:
        text_under_construction += f"Only R${flight.price} to fly from {flight.from_city}-{flight.from_airport_iata} to \
            {flight.to_city}-{flight.to_airport_iata} from {flight.departure_date} to {flight.arrival_date}. "
    message = client.messages.create(
        body=text_under_construction,
        from_=SMS_FROM,
        to=SMS_TO
    )
    return message.sid
