import json
import os

import urllib3

API_KEY = os.getenv("WEATHERAPI_KEY")
base_url = "https://api.weatherapi.com/v1/forecast.json"
client = urllib3.PoolManager()


def get_forcast(location, n_days):
    r = client.request("POST",
                       base_url,
                       fields=dict(key=API_KEY, q=location, days=n_days)
                       )
    response = r.data.decode('utf-8')
    result = json.loads(response)
    return result
