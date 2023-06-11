import requests
import datetime as dt
import os

GENDER = 'male'
WEIGHT_KG = '60'
HEIGHT_CM = '180'
AGE = '31'

APP_ID = 'yourAppID'
API_KEY = 'yourAPIKey'

# SHEETY_AUTH_TOKEN = 'someRandomSheetyAuthToken'

# Retrieve from User Environment Variables. All 3 methods below work.
# SHEETY_AUTH_TOKEN = os.environ.get('SHEETY_AUTH_TOKEN') 
# SHEETY_AUTH_TOKEN = os.getenv('SHEETY_AUTH_TOKEN') 
SHEETY_AUTH_TOKEN = os.environ['SHEETY_AUTH_TOKEN']

query_input = input('Tell me which exercises you did: ')

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/e5bf0a745960564a88ccb894e7d3adc3/myWorkouts/workouts'

exercise_params = {
    'query': query_input,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
# print(response)
# print(result)

current_datetime = dt.datetime.now()

exercise = result['exercises'][0]['name'].title()
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']
date = current_datetime.strftime('%m/%d/%Y')
time = current_datetime.strftime('%X')

body = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories,
    }
}

sheety_header = {
    'Authorization': f'Bearer {SHEETY_AUTH_TOKEN}'
}

add_row = requests.post(url=sheety_endpoint, json=body, headers=sheety_header)
print(add_row)
print(add_row.text)


# get_rows = requests.get(url=sheety_endpoint).json()
# print(get_rows)