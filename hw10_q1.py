"""
Author: Noa Kirschbaum
Assignment / Part: HW10 - Q1
Date due: 2022-05-05
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import random

class Weapon:
    def __init__(self, weapon_name, strength):
        self.weapon_name = weapon_name
        self.strength = strength

    def __str__(self):
        return "'{}' Weapon object (strength {}).".format(self.weapon_name, self.strength)

    def does_break(self):
        random_num = random.random()

        if (self.strength * 0.5) > random_num:
            return True
        else:
            return False

def main():
    some_weapon = Weapon("Rickenbacker 4003", 0.6)
    number_of_tests = 100
    number_of_breaks = 0

    # I'm testing this 100 times and keeping track of how many times it breaks
    for i in range(number_of_tests):
        if some_weapon.does_break():
            number_of_breaks += 1
    percentage = (number_of_breaks / number_of_tests) * 100
    print("The {} broke {}% of the time in {} tests!".format(some_weapon.weapon_name, round(percentage), number_of_tests))


if __name__ == '__main__':
    main()