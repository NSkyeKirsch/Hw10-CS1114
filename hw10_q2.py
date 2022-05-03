"""
Author: Noa Kirschbaum
Assignment / Part: HW10 - Q2
Date due: 2022-04-28
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from hw10_q1 import Weapon
import random

class Duelist:
    def __init__(self, duelist_name, weapon_inventory):
        self.duelist_name = duelist_name
        self.weapon_inventory = weapon_inventory
        self.number_of_weapons = len(weapon_inventory)

    def __str__(self):
        final_str = "Duelist object {}, carrying".format(self.duelist_name)
        for i in range(self.number_of_weapons):
            if i+1 == self.number_of_weapons:
                final_str += " and {} Weapon objects.".format(self.weapon_inventory[i].weapon_name)
            else:
                final_str += " {},".format(self.weapon_inventory[i].weapon_name)

        return final_str

    def get_winner_of_duel_name(self, opponent):

        if self.number_of_weapons > 0 and opponent.number_of_weapons > 0:

            duelist_weapon = self.weapon_inventory[random.randint(0,self.number_of_weapons-1)]
            print("Duelist {} picked a {}!".format(self.duelist_name, duelist_weapon.weapon_name))
            opponent_weapon = opponent.weapon_inventory[random.randint(0,opponent.number_of_weapons-1)]
            print("Duelist {} picked a {}!".format(opponent.duelist_name, opponent_weapon.weapon_name))

            if duelist_weapon.strength > opponent_weapon.strength:
                if not duelist_weapon.does_break():
                    return self.duelist_name
                else:
                    print("{}'s weapon broke!".format(self.duelist_name))
                    return opponent.duelist_name
            elif duelist_weapon.strength < opponent_weapon.strength:
                if not opponent_weapon.does_break():
                    return opponent.duelist_name
                else:
                    print("{}'s weapon broke!".format(opponent.duelist_name))
                    return self.duelist_name
            else:
                print("Both duelists picked weapons of the same strength! The winner will be decided purely by pseudo-randomly generenated numbers!")
                random_num = random.randint(1, 2)
                print("random number:", random_num)
                if random_num == 1:
                    return self.duelist_name
                else:
                    return opponent.duelist_name




        elif self.number_of_weapons > 0 and opponent.number_of_weapons <= 0:
            print("Only one duelist has a weapon!")
            return self.duelist_name
        elif opponent.number_of_weapons > 0 and self.number_of_weapons <= 0:
            print("Only one duelist has a weapon!")
            return opponent.duelist_name
        else:
            return "NO CONTEST."


def main():
    # Creating my Weapon objects
    weapon_1 = Weapon("Rickenbacker 4001c64", 0.8)
    weapon_2 = Weapon("Hofner 500/1", 0.6)
    weapon_3 = Weapon("Squier VI", 0.4)
    weapon_4 = Weapon("Rickenbacker 330", 0.8)
    weapon_5 = Weapon("Fender Vintera 60s Mustang", 0.6)
    weapon_6 = Weapon("Gretsch 6122", 0.4)
    # Creating my Duelist objects
    bass_player = Duelist("Aki Mizuguchi", [weapon_1, weapon_2, weapon_3])
    guitarist = Duelist("Yori Asanagi", [weapon_4, weapon_5, weapon_6])
    # Testing the get_winner_of_duel_name method of the Duelist object 'bass_player' a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner = bass_player.get_winner_of_duel_name(guitarist)
        print("THE WINNER OF DUEL #{} IS {}!".format(duel_number + 1, winner), end="\n\n")

if __name__ == '__main__':
    main()

