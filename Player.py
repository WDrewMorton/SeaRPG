class Player:
    '''
    '''
    def __init__(self, name="player", health_max=100, ap_max=10, oxygen=50, level=1, exp=0, items=[]):
        self.name = name
        self.health_max = health_max
        self.health = health_max
        self.ap_max = ap_max
        self.ability = ap_max
        self.oxygen = oxygen
        self.level = level
        self.exp = exp
        self.items = items
        # self.stats = {'STR': 3, 'INT': 3, 'ARM': 1}
        '''
        types of players
        Civilian: standard
        BookWorm: INT +2 STR -2
        Jock: STR +2 INT -2
        Surfer: Oxygen +10
        Biologist: Oxygen +5 INT +1 STR -1
        '''

    def attack(self):
        print("You attack! Huyaa!")

    def display(self):
        print("Name: {}, HP: {} / {}, AP:{} / {}\nItems: {}"
            .format(self.name, self.health, self.health_max, self.ap_max, self.ability, self.items))

    def level_up(self):
        self.level += 1
        self.health_max += 10
        self.health = self.health_max
        self.ap_max += 1
        self.ability = self.ap_max
        # self.oxygen += 5
