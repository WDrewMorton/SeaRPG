import random

class Player():
    '''
    '''
    def __init__(self, name="player", health_max=100, ap_max=10, oxygen=50, level=1, exp=0, items=[]):
        self.name = name
        self.health_max = health_max
        self.health = health_max
        self.ap_max = ap_max
        self.ap = ap_max
        self.oxygen = oxygen
        self.level = level
        self.exp = exp
        self.items = items
        self.stats = {'STR': 3, 'INT': 3, 'ARM': 1}#, 'WEP': "Fists"}
        '''
        types of players
        Civilian: standard
        BookWorm: INT +2 STR -2
        Jock: STR +2 INT -2
        Surfer: Oxygen +10
        Biologist: Oxygen +5 INT +1 STR -1
        '''

    def attack(self):
        roll = random.randint(self.level, self.level + self.stats.get("STR"))
        self.ap -= 1
        self.oxygen -= 1
        print("You attack! Huyaa!")
        return roll

    def display(self):
        print("Name: {}, Level: {}, Exp: {}, HP: {} / {}, AP:{} / {}\nItems: {}"
            .format(self.name, self.level, self.exp, self.health, self.health_max, self.ap, self.ap_max, self.items))

    def level_up(self):
        self.level += 1
        self.health_max += 10
        self.health = self.health_max
        self.ap_max += 1
        self.ap = self.ap_max
        # self.oxygen += 5
