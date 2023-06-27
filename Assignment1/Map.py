from City import City
from Route import Route
import csv
import sys
import heapq
import math


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
        self.__cities = cities

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

    def uniform_cost_search(self, starting_city_name):
        starting_city = self.get_cities()[starting_city_name]

        queue = [(0, starting_city)]
        visited_cities = {starting_city: 0}
        infection_order = []

        while queue:
            curr_cost, curr_city = heapq.heappop(queue)
            infection_order.append(curr_city)

            for route in curr_city.get_routes():
                next_city = route.get_destination(curr_city)
                new_cost = curr_cost + route.get_distance()

                if next_city not in visited_cities or new_cost < visited_cities[next_city]:
                    visited_cities[next_city] = new_cost
                    heapq.heappush(queue, (new_cost, next_city))

        return infection_order

    def a_star_search(self, starting_city_name, destination_name):
        starting_city = self.get_cities()[starting_city_name]
        destination_city = self.get_cities()[destination_name]

        queue = [(0, starting_city)]
        visited_cities = {starting_city: 0}
        total_route = []

        while queue:
            curr_cost, curr_city = heapq.heappop(queue)
            total_route.append(curr_city)

            if curr_city == destination_city:
                return total_route, curr_cost

            for route in curr_city.get_routes():
                next_city = route.get_destination(curr_city)
                new_cost = visited_cities[curr_city] + route.get_distance()

                if next_city not in visited_cities or new_cost < visited_cities[next_city]:
                    visited_cities[next_city] = new_cost
                    score = new_cost + Map.heuristic_haversine(next_city, destination_city)
                    heapq.heappush(queue, (score, next_city))

        return None

    @staticmethod
    def heuristic_haversine(next_city, destination):
        from_lat = next_city.get_latitude()
        from_long = next_city.get_longitude()
        to_lat = destination.get_latitude()
        to_long = destination.get_longitude()

        earth_radius_miles = 3958.8

        # Convert Long and Lat to radians
        next_lat_rad = math.radians(from_lat)
        next_long_rad = math.radians(from_long)
        dest_lat_rad = math.radians(to_lat)
        dest_long_rad = math.radians(to_long)

        a = pow(math.sin((next_lat_rad - dest_lat_rad)/2), 2) + math.cos(dest_lat_rad) * math.cos(next_lat_rad) * pow(math.sin((next_long_rad - dest_long_rad) / 2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return earth_radius_miles * c

    # String Override
    def __str__(self):
        cities = self.get_cities()
        ret = f"Map of {self.get_state()}\n------------------------------------------------------------\n"
        for city in cities:
            ret += f"{cities[city]}\n"
        return ret
