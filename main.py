import requests
from twilio.rest import Client


MY_API_KEY = 'yourAPIKey'
ANGELA_API_KEY = '69f04e4613056b159c2761a9d9e664d2'
MY_LAT = 33.659771
MY_LONG = -117.999313

end_point_url = f'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': ANGELA_API_KEY,
    'exclude': 'current,minutely,daily',
}
# Twilio account info
account_sid = 'yourTwilioAccountSID'
auth_token = 'yourTwilioAuthToken'

response = requests.get(url=end_point_url, params=parameters)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
# print(weather_data)

# weather_id = weather_data['hourly'][0]['weather'][0]['id']
# print(weather_id)


def check_if_umbrella(data: dict):
    """Check if an umbrella is needed for the next 12 hours."""
    for hour in data['hourly'][:12]:
        if hour['weather'][0]['id'] < 700:
            # print('Bring an Umbrella')
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body="It's going to rain today. Remember to brng an ☔",
                from_='+yourTwilioPhone#',
                to='+recipientPhone#'
            )
            print(message.status)
            return

    print('No umbrella needed today.')


check_if_umbrella(weather_data)
