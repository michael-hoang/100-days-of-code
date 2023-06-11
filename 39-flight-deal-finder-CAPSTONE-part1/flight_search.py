import requests
from pprint import pprint
import datetime as dt


LOCATION_API_ENDPOINT = 'https://api.tequila.kiwi.com/locations/query'
TEQUILA_API_KEY = 'yourTequilaAPIKey'


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    # def __init__(self):
    #     """Initializes properties for FlightSearch."""

    def search_city(self, city: str):
        """Search for a city data and returns the result."""
        header = {'apikey': TEQUILA_API_KEY}
        params = {'term': city}
        response = requests.get(url=LOCATION_API_ENDPOINT,
                                params=params,
                                headers=header)
        result = response.json()
        return result


if __name__ == '__main__':
    fs = FlightSearch()
