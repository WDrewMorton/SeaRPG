import Player
import Map
import random

name = input("Who dares enter the oceans?")
map_difficulty = int(input("Difficulty (0, 1, 2, 3)"))
if name.lower() == "merman":
    p = Player.Player(name, max_health=250, ability=100, oxygen=10000)
else:
    p = Player.Player(name)
m = Map.Map(difficulty=map_difficulty)


def get_hurt(character):
    attack_hit = random.randint(0, 1)
    if attack_hit:
        damage = random.randint(0, 20)
        character.health = character.health - damage


m.display()
p.display()
while p.health > 0:
    p.attack()
    m.mob_nums -= 1
    get_hurt(p)
    if m.mob_nums == 0 and p.health > 0:
        if m.floor % 5 == 0:
            print("LEVEL UP")
            p.level_up()
        print("Survived floor {}! On to the next one".format(m.floor))
        m.next_floor()
        m.display()
