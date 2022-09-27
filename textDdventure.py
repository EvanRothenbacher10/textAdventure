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
        print("          \033[0;32;40mLoading \n        [.]")
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
        sleep(1)
        clear()
        return " "

def startGame(x):
    if x == "Y":
        return loadingScrn()
    else:
        return "Error"

def conv1():
    print ("You put the bread in the toaster.")
    sleep(0.7)
    clear()
    print ("You put the bread in the toaster..")
    sleep(0.7)
    clear()
    print ("You put the bread in the toaster...")
    sleep(1)
    clear()
    return "Suddenly the toast jumps out and attacks you!"

def conv2():
    return "wip"

def firstQuestion(x):
    if x == "Y":
        return conv1()
    else:
        return conv2()

# Calls

clear()

print("\033[0;31;40m\n \n \n             WARNING: Game is case sensitive, all answers should be in Y/N format.")

sleep(5)

clear()

print(startGame(input("\033[0;37;40mDo you want to start the game? \n")))

clear()

print("\033[0;34;40m ")

for l in "You wake up in the morning feeling hungry":
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(random.random()*10.0/typing_speed)

sleep(0.2)

print(firstQuestion(input("\n\n\033[0;37;40mMake Breakfast? \n  ")))