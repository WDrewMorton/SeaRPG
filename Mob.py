import random

class Mob():

    def __init__(self, name="mob", health_max=10, ap_max=5, level=1, exp=5):
        self.name = name
        self.health_max = health_max
        self.health = health_max
        self.ap_max = ap_max
        self.ability = ap_max
        self.level = level
        self.exp = exp
        self.stats = {'STR': 1, 'INT': 1, 'ARM': 0}#, 'WEP': "Fists"}


    def attack(self):
        roll = random.randint(self.level, self.level + self.stats.get("STR"))
        print("You attack! Huyaa!")
        return roll

    def display(self):
        print("Name: {}, HP: {} / {}, AP:{} / {}\nItems: {}"
            .format(self.name, self.health, self.health_max, self.ap_max, self.ability, self.items))
