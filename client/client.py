# Клиент

import requests

url = 'http://192.168.77.77:8080/distance'
params = {'x1': 1, 'y1': 2, 'x2': 3, 'y2': 4}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    distance = data['distance']
    print(f'The distance between the points is {distance}')
else:
    print('Error:', response.status_code)
