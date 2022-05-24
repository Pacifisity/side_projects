"""
Combat Simulator Exercise

- Has a base class containing attributes that all characters have:  Hit points, name, minimum damage and maximum damage
- Should also contain certain actions (methods): attack, defend
-- defend should halve the amount of damage taken on next attack

- 2 sub-classes that inherit from the base class: player and monster
-- Player should contain attributes: health_potions to dictate how many healing potions they have at their disposal
-- Player should also have a unique method: heal.  It should heal a certain amount of health and also remove one potion from the inventory

-- Monster should contain attribute:  smokebombs
-- Monster should also contain method:  use_smokebomb, which prevents damage from the next player attack and also removes one from the inventory 
"""
import random

class Attributes:
    unique_names = set()

    def __init__(self):
        self.name = ""
        self.hit_points = 0
        self.minimum_damage = 0
        self.maximum_damage = 0
        self.utilities = None
        self.utility_type = ""
        self.class_type = ""

    def create(self):
        while True:
            self.name = str(input(f"{self.class_type}'s Name:\n"))
            if self.name not in Attributes.unique_names:
                Attributes.unique_names.add(self.name)
                break
            print("That name has been taken.")
        self.hit_points = int(input(f"{self.name}'s Hit Points:\n"))
        self.maximum_damage = int(input(f"{self.name}'s Maximum Damage:\n"))
        self.minimum_damage = int(input(f"{self.name}'s Minimum Damage:\n"))
        self.utilities = int(input(f"{self.name}'s {self.utility_type}:\n"))

    def attack(self, opponent):
        damage = random.randint(self.minimum_damage, self.maximum_damage)
        return damage
        
    def defend(self, damage):
        damage = damage / 2
        return damage

class Cleric(Attributes):
    def __init__(self):
        self.class_type = "Cleric"
        self.utility_type = "Health Potions"
    
    def utility(self):
        return "Health Potions"

    def heal(self):
        pass

class Rogue(Attributes):
    def __init__(self):
        self.class_type = "Rogue"
        self.utility_type = "Smokebombs"

    def utility(self):
        return "Smokebombs"

    def smokebomb(self):
        pass

classes = {
    1: Cleric,
    2: Rogue,
}


players = {}
used_names = set()
class_string = " ".join([f"{i} - {v.__name__}\n" for i, v in classes.items()])

number_of_players = int(input("How many players?:\n"))

for player in range(number_of_players):
    player_class_input = int(input(f"Choose a class:\n {class_string}"))
    player = classes[player_class_input]()
    player.create()
    players[player.name] = player

# while True: # Fight Scenario
#     pass