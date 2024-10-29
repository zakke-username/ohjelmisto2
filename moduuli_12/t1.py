import requests

kysely = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(kysely).json()
vitsi = vastaus["value"]
print(vitsi)