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
        return "preinted2"

# Calls

clear()

print("\033[0;31m\n \n        WARNING: Game is case sensitive, all answers should be in Y/N format.")

sleep(5)

clear()

print(startGame(input("\033[0;37mDo you want to start the game? \n")))

print("You wake up feeling hungry...", end=".")

print(firstQuestion(input(" Make toast?")))