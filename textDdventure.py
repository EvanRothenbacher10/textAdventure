import os
from os import *
import time
from time import *

# Variables


# Functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loadingScrn():
        print("         Loading \n         .")
        sleep(.5)
        clear()
        print("         Loading \n         ..")
        sleep(.5)
        clear()
        print("         Loading \n         ...")
        sleep(.5)
        clear()
        print("         Loading \n         ....")
        sleep(.5)
        clear()
        print("         Loading \n         .....")
        sleep(.5)
        clear()
        print("         Loading \n         ......")
        sleep(.5)
        clear()
        print("         Loading \n         .......")

def startGame(x):
    if x == "Y":
        return loadingScrn()
    else:
        return "Error"

# Calls

clear()

print("WARNING: Game is case sensitive, all answers should be in Y/N format.")

sleep(5)

clear()

print(startGame(input("Do you want to start the game? \n")))