from flight_api import FlightSearch, FLIGHT_FROM
from flight_data import FlightData
from sms_api import send_sms
from sheety_api import SheetRequest


# GET ALL SHEETY DATA:
sheety_request_01 = SheetRequest()
all_sheety_data = sheety_request_01.get_all_data()

# CHECK FOR EMPTY IATA FIELDS:
for n in range(len(all_sheety_data)):
    this_destination = all_sheety_data[n]
    if not this_destination["iataCode"]:
        fs = FlightSearch(this_destination["city"])
        this_iata_city = fs.search_city_iata()
        this_destination["iataCode"] = this_iata_city
        sheety_request_01.edit_row(
            row_num=this_destination["id"], new_content=this_destination)

# GET UPDATED SHEET FROM SHEETY:
sheety_request_02 = SheetRequest()
sheety_updated_data = sheety_request_02.get_all_data()


# CHECK FOR CHEAP FLIGHTS:
cheapest_flights = []
for destination in sheety_updated_data:
    flight_search_obj = FlightSearch(flight_to_city=destination["iataCode"])
    flight_search_result = flight_search_obj.flight_search(to_airport_iata=destination["iataCode"],
                                                           max_price=destination["maximumPrice"])
    try:
        flight_data = FlightData(whole_data=flight_search_result)
    except:
        print(
            f"No flights found from {FLIGHT_FROM} to {flight_search_obj.flight_to_city}.")
    else:
        cheapest_flights.append(flight_data)

if not cheapest_flights:
    print("No cheap flights were found. Nothing to SMS.")
else:
    send_sms(cheapest_flights)
