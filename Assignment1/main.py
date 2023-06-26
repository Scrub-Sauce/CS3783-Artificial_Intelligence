from Map import Map

if __name__ == "__main__":
    basePath = "files/"

    map = Map()

    map.load_map(basePath)

    print(map)