import requests

api_key = ""

city = input("Enter a city: ")

coords_request = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
coords_response = requests.get(coords_request).json()
latitude = coords_response[0]["lat"]
longitude = coords_response[0]["lon"]

weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
weather_response = requests.get(weather_request).json()

weather = weather_response["weather"][0]["main"]
temp = weather_response["main"]["temp"]

print(f"Weather in {city}: {weather}, temperature: {temp} °C")