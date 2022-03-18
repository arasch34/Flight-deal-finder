import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9b00fd9b054ad1b75fd40b06e79f5bdf/dealsOnFlights/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in google sheet
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # update the Google Sheet with the IATA codes
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
