import requests
from datetime import datetime

USERNAME = 'userName'
TOKEN = 'yourRandomAuthenticationToken'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

## Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# >>> {"message":"Success. Let's visit https://pixe.la/@userName , it is your profile page!","isSuccess":true}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai',
}
# # Create graph
# # Need to provide authentication token before we can make a post request. Do this by
# # using headers. 
headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

## Post a Pixel to the graph

postPixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()
# print(today)

postPixel_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many kilometers did you cycle today? '),
}

response = requests.post(url=postPixel_endpoint, json=postPixel_params, headers=headers)
print(response.text)


## Updating a pixel
updatePixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221109'

updatePixel_params = {
    'quantity': '5',
}

# response = requests.put(url=updatePixel_endpoint, json=updatePixel_params, headers=headers)
# print(response.text)


## Delete a pixel
deletePixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221109'

# response = requests.delete(url=deletePixel_endpoint, headers=headers)
# print(response.text)
