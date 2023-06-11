import requests
from pprint import pprint
import datetime as dt
from data_manager import DataManager


SEARCH_FLIGHT_API_ENDPONIT = 'https://api.tequila.kiwi.com/v2/search'
TEQUILA_API_KEY = 'yourTequilaAPIKey'


class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self, depart_iata: str):
        """Initialize FlightData attributes."""
        self.departure_iata = depart_iata
        self.destination_price = {}

        self.get_destination_price()

    def get_destination_price(self):
        """
        Retrieve destinations from Google Sheet and then search for the flight
        on Tequila.
        """
        dm = DataManager()  # Contains destination data from Google Spreadsheet
        destination_data = dm.destination_data
        for row_dict in destination_data:
            try:
                try:
                    iata_code = row_dict['IATA Code']
                    city = row_dict['City']
                    current_price, arrival_iata, o_date, i_date, b_link = self._search_flight(
                        depart_iata=self.departure_iata,
                        destin_iata=iata_code)
                    self.destination_price[city] = {}
                    self.destination_price[city]['IATA Code'] = arrival_iata
                    self.destination_price[city]['Price'] = current_price
                    self.destination_price[city]['Outbound Date'] = o_date
                    self.destination_price[city]['Inbound Date'] = i_date
                    self.destination_price[city]['Booking Link'] = b_link
                except (IndexError, KeyError):
                    iata_code = row_dict['IATA Code']
                    city = row_dict['City']
                    current_price, arrival_iata, o_date, i_date, b_link = self._search_flight(
                        depart_iata=self.departure_iata,
                        destin_iata=iata_code, stop_overs=1)
                    self.destination_price[city] = {}
                    self.destination_price[city]['IATA Code'] = arrival_iata
                    self.destination_price[city]['Price'] = current_price
                    self.destination_price[city]['Outbound Date'] = o_date
                    self.destination_price[city]['Inbound Date'] = i_date
                    self.destination_price[city]['Booking Link'] = b_link

            except (IndexError, KeyError):
                pass

    def _search_flight(self, depart_iata: str, destin_iata: str, stop_overs=0) -> str:
        """Search for flights between departure location and destination. Returns
        cheapest price, arrival IATA, outbound date, and inbound date.
        """
        tomorrow = dt.datetime.today() + dt.timedelta(days=1)
        sixMonth = tomorrow + dt.timedelta(days=180)
        header = {'apikey': TEQUILA_API_KEY}
        params = {
            'fly_from': depart_iata,
            'fly_to': destin_iata,
            'date_from': dt.datetime.strftime(tomorrow, '%d/%m/%Y'),
            'date_to': dt.datetime.strftime(sixMonth, '%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'max_stopovers': stop_overs,  # 0 is direct flights only
            'curr': 'USD',
            'asc': 1,  # ascending order from cheapest to most expensive
            'limit': 1,
        }
        response = requests.get(url=SEARCH_FLIGHT_API_ENDPONIT,
                                params=params,
                                headers=header)
        flight_data = response.json()
        price = flight_data['data'][0]['price']
        arrival_iata = flight_data['data'][0]['flyTo']
        outbound_date = flight_data['data'][0]['route'][0]['local_departure']
        inbound_date = flight_data['data'][0]['route'][1]['local_departure']
        booking_link = flight_data['data'][0]['deep_link']
        # format outbound and inbound dates
        outbound_date = outbound_date.split('T')
        outbound_date = outbound_date[0].split('-')
        outbound_date = f'{outbound_date[1]}-{outbound_date[2]}-{outbound_date[0]}'

        inbound_date = inbound_date.split('T')
        inbound_date = inbound_date[0].split('-')
        inbound_date = f'{inbound_date[1]}-{inbound_date[2]}-{inbound_date[0]}'

        return price, arrival_iata, outbound_date, inbound_date, booking_link


if __name__ == '__main__':
    departure_location = 'LAX'
    fd = FlightData(depart_iata=departure_location)
    pprint(fd.destination_price)
