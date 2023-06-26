class Route:
    def __init__(self, city1, city2, distance):
        self.__cities = [city1, city2]
        self.__distance = distance

    # Accessors
    def get_cities(self):
        return self.__cities

    def get_distance(self):
        return self.__distance

    # Mutators
    def set_cities(self, cities):
        self.__cities = cities

    def set_distance(self, distance):
        self.__distance = distance

    # String Override
    def __str__(self):
        cities = self.get_cities()
        ret = f"   {cities[0].get_city_name()}, {cities[1].get_city_name()}, {self.get_distance()}"
        return ret
