from geopy.geocoders import Nominatim


class LocationData:
    def __init__(self, country, city):
        self.location_params = {
            "city": city,
            "country": country,
        }

    def data(self):
        geolocator = Nominatim(user_agent="app")
        location = geolocator.geocode(self.location_params)
        if location is None:
            raise Exception("Please check if you wrote the name of the country and city correctly ")
        return location.latitude, location.longitude
