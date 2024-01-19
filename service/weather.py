from client import weatherapi
from dataclasses import dataclass, asdict
import datetime


def get_3day_forecast(location):
    api_data = weatherapi.get_forcast(location, 3)
    today = datetime.date.today()
    night_time = 23
    day_time = 12
    forecasts = api_data['forecast']['forecastday']
    f_night = [forecasts[x]["hour"][night_time] for x in range(3)]
    f_day = [forecasts[x]["hour"][day_time] for x in range(3)]
    result = [WeatherForcast((today+datetime.timedelta(days=x)).strftime('%d-%m-%Y'),
                             (today+datetime.timedelta(days=x)).strftime('%A'),
                             f_day[x]["temp_c"],
                             f_night[x]["temp_c"],
                             f_day[x]["condition"]["text"],
                             f_night[x]["condition"]["text"])
              .__dict__ for x in range(3)]
    return result


@dataclass
class WeatherForcast:
    dt: str
    day_name: str
    day_temp: str
    night_temp: str
    day_condition: str
    night_condition: str

    @property
    def __dict__(self):
        return asdict(self)
