import Player
import Map
import Mob
import random

# name = input("Who dares enter the oceans?")
# map_difficulty = int(input("Difficulty (0, 1, 2, 3)"))
name = "Drew"
map_difficulty = 0
if name.lower() == "merman":
    p = Player.Player(name, max_health=250, ap_max=100, oxygen=10000)
else:
    p = Player.Player(name)
m = Map.Map(difficulty=map_difficulty)
p = Player.Player()
m = Map.Map()


def get_hurt(character):
    attack_hit = random.randint(0, 1)
    if attack_hit:
        damage = random.randint(0, 20)
        character.health = character.health - damage

m.display()
m.create_map()
### FOR TESTING ONLY ###
print("display")
print("create map")
### FOR TESTING ONLY ###

# while p.health > 0: # and p.position not "X":
#     p.attack()
#     m.mob_nums -= 1
#     get_hurt(p)
#     if m.mob_nums == 0 and p.health > 0:
#         if m.floor % 5 == 0:
#             print("LEVEL UP")
#             p.level_up()
#         print("Survived floor {}! On to the next one".format(m.floor))
#         m.next_floor()
#         m.display()
def make_move():
    directions = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}
    while True:
        try:
            move_input = input("Which way will you go? (u, d, l, r): ").lower().strip()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if move_input.lower() not in directions.keys():
            print("You may only move u,d,l,r")
            continue
        else:
            return directions.get(move_input)
            break


def combat(p, mob):
    while mob.health > 0:
        if p.ap > 0:
            player_roll = p.attack()

            mob_roll = mob.attack()
            if player_roll > mob.stats.get("ARM"):
                print("Mob has been hurt")
                mob.health -= player_roll - mob.stats.get("ARM")
            else:
                print("player has missed")
            if mob_roll > p.stats.get("ARM"):
                print("Player has been hurt")
                p.health -= mob_roll - p.stats.get("ARM")
            else:
                print("mob has missed")
        else:
            if random.randint(0,1) == 1:
                print("Second Wind gathered during combat")
                p.ap = int(.10 * p.ap_max)
            else:
                print("Too tired to fight GET FUCKED")
### FOR TESTING ONLY ###
    # p.ap = p.ap_max
### FOR TESTING ONLY ###


def check_level_up():
    if p.exp > 100:
        p.level_up()
        p.exp -= 100


'''
so i want to increase by 10% of missing ap
3/100
10% of 7 is .7 so that would increase by 1
for now we'll just increase by 1 for every step you take that's not fighting
'''
def restore_ap():
    if p.ap < p.ap_max:
        print("Restoring some AP")
        # p.ap = p.ap + int((p.ap_max - p.ap) * .1)
        p.ap += 1



entrance_message = "Where you be? Oh you begin at the [E]ntrance " \
    + "and must find the E[x]it! Once you move from the entrance you'll " \
    + "see yourself as the [P]layer E and must reach the X \n"
print(entrance_message)
while p.health > 0 and p.oxygen > 0:
    direction = make_move()
    m.map_update(direction)
    if m.get_coords().get("P") == m.get_coords().get("X"):
        print("player has reached exit")
        p.exp = p.exp + 10
        check_level_up()
        m.next_floor()
    elif m.get_coords().get("P") in m.get_coords().get("M"):
        print("COMBAT LET'S GET TO FIGHTING!")
        mob = Mob.Mob()
        combat(p, mob)
        if p.health < 0:
            break
        else:
            print("pXP {}, mXP {}".format(p.exp, mob.exp))
            p.exp += mob.exp
            m.get_coords().get("M").remove(m.get_coords().get("P"))
            # remove mob after defeat
            check_level_up()
    else:
        restore_ap()
    print(p.display())
