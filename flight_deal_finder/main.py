from flight_api import FlightSearch, FLIGHT_FROM
from flight_data import FlightData
from sms import send_sms


TEST_DATA = {
    "LAX": 3500,
    "NYC": 4000
}

cheapest_flights = []

for iata_dest_city, estimated_price in TEST_DATA.items():
    fs001 = FlightSearch(iata_dest_city, estimated_price)
    search_result = fs001.flight_search()

    try:
        flight_data = FlightData(search_result)
    except:
        print(f"No flights found from {FLIGHT_FROM} to {iata_dest_city}")
    else:
        cheapest_flights.append(flight_data)

if not cheapest_flights:
    print("No cheap flights were found. Nothing to SMS.")
else:
    send_sms(cheapest_flights)