import requests


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "8cfe5875a006d90c6c2b62ca32f1f1b9"


class WeatherData:
    def __init__(self, lat, lon):
        self.weather_params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "cnt": 4,
        }

    def data(self):
        response = requests.get(OWN_Endpoint, params=self.weather_params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
