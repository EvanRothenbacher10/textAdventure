import os
from os import *
import time
from time import *
import threading
from threading import Thread
import sys
from sys import *
import random


# Variables

typing_speed = 50

# Functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loadingScrn():
        clear()
        print("          Loading \n        [.]")
        sleep(.5)
        clear()
        print("          Loading \n        [..]")
        sleep(.5)
        clear()
        print("          Loading \n        [...]")
        sleep(.5)
        clear()
        print("          Loading \n        [....]")
        sleep(.5)
        clear()
        print("          Loading \n        [.....]")
        sleep(.5)
        clear()
        print("          Loading \n        [......]")
        sleep(.5)
        clear()
        print("          Loading \n        [.......]")
        sleep(.5)
        clear()
        print("          Loading \n        [........]")
        sleep(.5)
        clear()
        print("          Loading \n        [.........]")
        sleep(.5)
        clear()
        print("     Loading Complete \n        [.........]")
        return " "

def startGame(x):
    if x == "Y":
        return loadingScrn()
    else:
        return "Error"

def introSequence():
    for l in "\n\n":
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(random.random()*10.0/typing_speed)

def firstQuestion():
    print("")

# Calls

clear()

print("\n \n \n             WARNING: Game is case sensitive, all answers should be in Y/N format.")

sleep(2.5)

clear()

print(startGame(input("Do you want to start the game? \n")))

clear()

sleep(1.5)

introSequence()