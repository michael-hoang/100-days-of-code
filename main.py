# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from flight_data import FlightData
from notification_manager import NotificationManager


dm = DataManager()
gs_data = dm.destination_data
fs = FlightSearch()

departure_city = 'Los Angeles'
depart_city_data = fs.search_city(city=departure_city)
departure_iata = depart_city_data['locations'][0]['code']


# Update missing IATA Code on Google Sheet
for row_dict in gs_data:
    if row_dict['IATA Code'] == '':
        city = row_dict['City']
        city_data = fs.search_city(city)
        airport_iata = city_data['locations'][0]['code']
        rowNum = dm.sheet.col_values(1).index(city) + 1
        dm.sheet.update(f'B{rowNum}', airport_iata)

# Compare Google Sheet prices with currently cheapest price for all the cities
# and send notification.
message = ''
fd = FlightData(depart_iata=departure_iata)
for k, v in fd.destination_price.items():
    city = k

    for row_dict in gs_data:
        if city == row_dict['City']:
            iata_code = v['IATA Code']
            current_price = float(v['Price'])
            gs_price = float(row_dict['Lowest Price'])
            outbound_date = v['Outbound Date']
            inbound_date = v['Inbound Date']
            booking_link = v['Booking Link']

            if current_price <= gs_price:
                message += f'Low price alert! Only ${current_price} to fly from \
{departure_city}-{departure_iata} to {city}-{iata_code}, from {outbound_date} \
to {inbound_date}.\n{booking_link}\n\n'

nm = NotificationManager()
nm.telegram_bot_sendtext(bot_message=message)

formatted_emailMessage = f'Subject:Flight Deal Notification\n\n{message}'
for email in dm.memberEmails:
    nm.send_email(email_address=email,
                  email_message=formatted_emailMessage)
