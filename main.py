from location_data import LocationData
from weather_data import WeatherData


location_country = input("country: ")
location_city = input("city: ")

location = LocationData(location_country, location_city)
location_data = location.data()

lat = location_data[0]
lon = location_data[1]

weather = WeatherData(lat, lon)
weather_data = weather.data()


def check_will_rain():
    will_rain = False

    for hour in weather_data["list"]:
        condition_code = hour["weather"][0]["id"]
        if condition_code < 700:
            will_rain = True

    if will_rain:
        print("better take an umbrella")

    else:
        print("it probably won't rain")


if __name__ == "__main__":
    check_will_rain()
