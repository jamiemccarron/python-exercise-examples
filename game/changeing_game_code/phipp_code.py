#!/usr/bin/env python

import sys


def getUserChoice(maxChoices):
    while True:
        answer = input("Enter your choice")
        choice = int(answer)
        if choice <= 0:
            print("Invalid choice try again")
        elif choice > maxChoices:
            print("Invalid choice out of range")
        else:
            return choice

sentinal = None

def room1():
    print("There is money in the box")
    print("1: take money from box")
    print("2: be a good person and dont take money from the box")

    choice = getUserChoice (2)
    if choice == 1:
        return 2
    else:
        return 3

def room2():
    print("The troll is about to attack you")
    print("1: fight")
    print("2: run away")

    choice = getUserChoice (2)
    if choice == 1:
        return 4
    else:
        return 3


def room3():
    print("You have dinner with your family")
    print ("Game over")
    sys.exit(0)


def room4():
    print("You got wounded and died")
    print ("Game over")
    sys.exit(0)


dungeon = [room1, room2, room3, room4]

def main():
    print("starting the game")

    index = 0
    while True:
        room = dungeon[index]
        nextRoom = room ()
        index = nextRoom - 1


if __name__ == "__main__":
    main()