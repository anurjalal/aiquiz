import os
import requests

API_KEY = os.getenv("WEATHERAPI_KEY")
base_url = "https://api.weatherapi.com/v1/forecast.json"


def get_forcast(location, n_days):
    response = requests.post("https://api.weatherapi.com/v1/forecast.json", dict(key=API_KEY, q=location, days=n_days))
    return response.json()
