from Map import Map

if __name__ == "__main__":
    basePath = "files/"

    texas_map = Map.get_map_instance()
    texas_map.load_map(basePath)
    print(texas_map)

    uninformed_infection_order = texas_map.uniform_cost_search("Three Rivers")
    ret = "Uninformed Infection Order - Uniform Cost Search\n------------------------------------\n"
    i = 1
    for city in uninformed_infection_order:
        ret += f"{i}. {city.get_city_name()}\n"
        i += 1
    print(ret)

    informed_route_order, distance = texas_map.a_star_search("San Antonio", "College Station")
    ret = "Informed Route Order - A* Search\n------------------------------------\n"
    i = 1
    for city in informed_route_order:
        ret += f"{i}. {city.get_city_name()}\n"
        i += 1
    ret += f"Total Distance: {distance}"
    print(ret)


