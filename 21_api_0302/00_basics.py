import requests
from datetime import datetime

url = "https://yahoo-weather5.p.rapidapi.com/weather"

querystring = {
    "location": "minsk",
    "format": "json",
    "u": "c"
}

headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()
weather = response['current_observation']['condition']
forecasts = response['forecasts']
print(f'Weather in {response["location"]["city"]}: {weather["temperature"]} C, {weather["text"]}')

for forecast in forecasts:
    print(f'{datetime.fromtimestamp(forecast["date"])}, '
          f'Day temp: {forecast["high"]}, '
          f'Night temp: {forecast["low"]} '
          f'Weather is {forecast["text"]}')
