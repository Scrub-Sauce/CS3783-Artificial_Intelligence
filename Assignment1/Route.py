class Route:
    def __init__(self, city1, city2, distance):
        self.__cities = [city1, city2]
        self.__distance = distance

    # Accessors
    def get_cities(self):
        return self.__cities

    def get_distance(self):
        self.get_distance()

    # Mutators
    def set_cities(self, cities):
        self.__cities = cities

    def set_distance(self, distance):
        self.__distance = distance

    # String Override
    def __str__(self):
        cities = self.get_cities()
        ret = f"""{cities[0]}, {cities[1]}, {self.get_distance()}"""