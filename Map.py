import random


class Map:

    map_list = []
    coords = {}

    def __init__(self, difficulty=0, floor=0, sunken_door=False):
        self.difficulty = difficulty
        self.sunken_door = sunken_door
        self.floor = floor
        self.mob_nums = 5 * difficulty + random.randint(1, 5)
        # self.create_map()

    def set_map_list(self, map_list):
        self.map_list = map_list

    def get_map_list(self):
        return self.map_list

    def set_coords(self, coords):
        self.coords = coords

    def get_coords(self):
        return self.coords

    def display(self):
        print("Difficulty: {}\nSunken Door: {}\nFloor: {}\nMobs: {}"
          .format(self.difficulty, self.sunken_door,
          self.floor, self.mob_nums))

    def next_floor(self):
        # self.sunken_door = (self.difficulty > 1 and (random.randint(0, 4) == 4))
        self.floor += 1
        self.mob_nums = self.floor + 5 * self.difficulty + random.randint(1, 5)
        self.create_map()

    def create_map(self):
        row = random.randint(4, 8)
        col = random.randint(5, 8)
        map_list = [[" "] * col for i in range(row)]
        self.set_map_list(map_list)
        mob_list = [() for x in range(self.mob_nums)]

        # E = Entrance, X = Exit, R = Random Event, M = Monster
        coords = {"E": (), "X": (), "M": mob_list} #, "R": (), "M": ()}
        for i in coords.keys():
            if i != "M":
                r = random.randint(0, row-1)
                c = random.randint(0, col-1)
                r_c = (r, c)
                while r_c in coords.values() or r_c in coords["M"]:
                    print("Already here genius!")
                    r = random.randint(0, row-1)
                    c = random.randint(0, col-1)
                    r_c = (r, c)
                    # re-get coords
                coords[i] = r_c
                map_list[r][c] = i
            else:
                coordsM = coords["M"]
                for x in range(len(coordsM)):
                    r = random.randint(0, row-1)
                    c = random.randint(0, col-1)
                    r_c = (r, c)
                    while r_c in coords.values() or r_c in coords["M"]:
                        print("Already here genius!")
                        r = random.randint(0, row-1)
                        c = random.randint(0, col-1)
                        r_c = (r, c)
                        # re-get coords
                    # coords.get("M")[x] = r_c
                    coordsM[x] = r_c
                    ### For testing only ###
                    map_list[r][c] = i
                    ### For testing only ###



        coords.update({"P": coords.get("E")})
        self.set_coords(coords)
        self.map_display(self.get_map_list())


    def map_display(self, map_list):
        for x in map_list:
            print(x)
    def exit(self):
        coords = self.get_coords()
        if coords["P"] == coords["X"]:
            return False
    def map_update(self, direction):
        coord = self.get_coords()
        map_list = self.get_map_list()
        p_coord = coord["P"]
        r = p_coord[0] + direction[0]
        c = p_coord[1] + direction[1]
        if r > (len(map_list) - 1) or r < 0 or c < 0 or c > (len(map_list[0]) - 1):
            print("invalid move")
            return
        r_c = (r, c)
        # if r_c in coord["M"]:
        #     print("Start Combat")
        coord["P"] = r_c
        if map_list[p_coord[0]][p_coord[1]] != "E":
            map_list[p_coord[0]][p_coord[1]] = "~"
        map_list[r][c] = "P"
        self.set_map_list(map_list)
        self.set_coords(coord)
        print("Updating Map!")
        self.map_display(self.get_map_list())
        # print(get_map_list())
