class FlightData:

    def __init__(self, whole_data) -> None:
        self.whole_cheapest_data = whole_data["data"][0]
        self.price = self.whole_cheapest_data["price"]
        self.from_city = self.whole_cheapest_data["cityFrom"]
        self.from_airport_iata = self.whole_cheapest_data["flyFrom"]
        self.to_city = self.whole_cheapest_data["cityTo"]
        self.to_airport_iata = self.whole_cheapest_data["flyTo"]
        self.departure_date = self.whole_cheapest_data["local_departure"][0:9]
        self.arrival_date = self.whole_cheapest_data["route"][1]["local_arrival"][0:9]
