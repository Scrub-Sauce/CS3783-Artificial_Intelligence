from City import City
from Route import Route
import csv
import sys
class Map:

    __instance = None

    def __init__(self):
        self.__state = "Texas"
        self.__cities = {}
        if Map.__instance is not None:
            raise Exception("Map is a singleton and can only be instantiated once")
        Map.__instance = self

    # Map Singleton
    @staticmethod
    def get_map_instance():
        if Map.__instance is None:
            Map.__instance = Map()
        return Map.__instance

    # Accessors
    def get_state(self):
        return self.__state

    def get_cities(self):
        return self.__cities

    # Mutators
    def set_state(self, state):
        self.__state = state

    def set_cities(self, cities):
        self.__cities= cities

    # Helper Methods
    # def uninformed_search(self):

    # def informed_search(self):

    def load_map(self, path):

        cities_file = f"{path}cities.csv"

        try:
            cities = self.get_cities()
            with open(cities_file) as csv_infile:
                cities_csv_reader = csv.reader(csv_infile)
                for row in cities_csv_reader:
                    tmp_city = City(row[0], row[1], row[2])
                    cities[tmp_city.get_city_name()] = tmp_city
        except FileNotFoundError:
            sys.stderr.write(f'''cities.csv not found at {cities_file}''')
            exit(1)

        distances_file = f"{path}distances.csv"
        try:
            with open(distances_file) as csv_infile:
                distances_csv_reader = csv.reader(csv_infile)
                for row in distances_csv_reader:
                    tmp_route = Route(cities[row[0]], cities[row[1]], row[2])
                    cities[row[0]].add_route(tmp_route)
                    cities[row[1]].add_route(tmp_route)
        except FileNotFoundError:
            sys.stderr.write(f'''distances.csv not found at {distances_file}''')
            exit(1)

    # String Override
    def __str__(self):
        cities = self.get_cities()
        ret = f"Map of {self.get_state()}\n------------------------------------------------------------\n"
        for city in cities:
            ret += f"{cities[city]}\n"
        return ret
