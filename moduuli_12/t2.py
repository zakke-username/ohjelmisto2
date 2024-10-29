import requests
import json

api_key = ""

city = input("Anna kaupungin nimi: ")

coords_request = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
coords_response = requests.get(coords_request).json()
latitude = coords_response[0]["lat"]
longitude = coords_response[0]["lon"]

weather_request = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={api_key}"
weather_response = requests.get(weather_request).json()
print(json.dumps(weather_response))