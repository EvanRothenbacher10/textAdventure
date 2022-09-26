import os
from os import *
import time
from time import *
import threading
from threading import *

# Variables


# Functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loadingScrn():
        clear()
        print("\n         \033[0;32mLoading \n        [.]")
        sleep(.5)
        clear()
        print("\n         Loading \n        [..]")
        sleep(.5)
        clear()
        print("\n         Loading \n        [...]")
        sleep(.5)
        clear()
        print("\n         Loading \n        [....]")
        sleep(.5)
        clear()
        print("\n         Loading \n        [.....]")
        sleep(.5)
        clear()
        print("\n         Loading \n        [......]")
        sleep(.5)
        clear()
        print("\n         Loading \n        [.......]")
        sleep(.5)
        clear()
        print("\n     Loading Complete \n        [.......]\033[0;37m")
        sleep(0.5)
        clear()
        return " "

def startGame(x):
    if x == "Y":
        return loadingScrn()
    else:
        return "Error"

def firstQuestion(x):
    if x == "Y":
        clear()
        print("You put bread in the toaster")
        sleep(.7)
        clear()
        print("You put bread in the toaster.")
        sleep(.7)
        clear()
        print("You put bread in the toaster..")
        sleep(.7)
        clear()
        print("You put bread in the toaster...")
        sleep(1.5)
        clear()
        return "Suddenly toast leaps out of the toaster and starts attacking you!"

def firstBattle(x):
    if x == "Fight":
        clear()
        print("You decide to fight the piece of Toast")
    elif x == "Run":
        clear()
        print("You attempt to run")
    else:
        clear()
        firstBattle()

# Calls

clear()

print("\033[0;31m\n \n        WARNING: Game is case sensitive, all answers should match given prompt.")

sleep(5)

clear()

print(startGame(input("\033[0;37mDo you want to start the game? \n")))

print("You wake up feeling hungry...", end=".")

print(firstQuestion(input(" Make toast?\n")))

sleep(0.7)

print(firstBattle(input("Do you fight the toast? \n")))