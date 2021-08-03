import random


class Map:

    def __init__(self, difficulty=0, floor=0, sunken_door=False):
        self.difficulty = difficulty
        self.sunken_door = sunken_door
        self.floor = floor
        self.mob_nums = 5 * difficulty + random.randint(1, 5)
        self.create_map()

    def display(self):
        print("Difficulty: {}\nSunken Door: {}\nFloor: {}\nMobs: {}"
          .format(self.difficulty, self.sunken_door,
          self.floor, self.mob_nums))

    def next_floor(self):
        self.sunken_door = (self.difficulty > 1 and (random.randint(0, 4) == 4))
        self.floor += 1
        self.mob_nums = self.floor + 5 * self.difficulty + random.randint(1, 5)



    def create_map(self):
        row = random.randint(4, 8)
        col = random.randint(5, 8)
        map_list = [[" "] * col for i in range(row)]
        set_map_list(map_list)

        # E = Entrance, X = Exit, R = Random Event, M = Monster
        coords = {"E": (), "X": ()}#, "R": (), "M": ()}
        used_coords = []

        for i in coords.keys():
            r = random.randint(0, row-1)
            c = random.randint(0, col-1)
            r_c = (r, c)
            while r_c in coords.values():
                print("Already here genius!")
                r = random.randint(0, row-1)
                c = random.randint(0, col-1)
                r_c = (r, c)
                # re-get coords
            coords[i] = r_c
            map_list[r][c] = i
        coords.update({"P": coords.get("E")})
        map_display(map_list)

def map_display(map_list):
    for x in map_list:
        print(x)

def set_map_list(self, map_list):
    self.map_list = map_list


def get_map_list(self):
    return self.map_list

def map_update(direction):
    print("Updating Map!")
    print(get_map_list())
