class City:
    def __init__(self, city_name, latitude, longitude):
        self.__city_name = city_name
        self.__latitude = latitude
        self.__longitude = longitude
        self.__routes = []

    # Accessors
    def get_city_name(self):
        return self.__city_name

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude

    def get_routes(self):
        return self.__routes

    # Mutators
    def set_city_name(self, city_name):
        self.__city_name = city_name

    def set_latitude(self, latitude):
        self.__latitude = latitude

    def set_longitude(self, longitude):
        self.__longitude = longitude

    def set_routes(self, routes):
        return self.__routes

    # Helper Methods
    def check_lat_pole(self):
        latitude = self.get_latitude()
        if latitude < 0:
            return f"{abs(latitude)} S"
        else:
            return f"{abs(latitude)} N"

    def check_long_pole(self):
        longitude = self.get_longitude()
        if longitude < 0:
            return f"{abs(longitude)} W"
        else:
            return f"{abs(longitude)} E"

    # String Override
    def __str__(self):
        ret = f"""{self.get_city_name()}, {self.check_lat_pole()}, {self.check_long_pole()}\nRoutes:"""
        for route in self.get_routes():
            ret += f"{route}\n"
        return ret
