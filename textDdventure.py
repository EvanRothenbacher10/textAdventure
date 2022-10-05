import os
from os import *
import time
from time import *
import threading
from threading import *
import random
from random import *
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

def startGame(ans1):
    if ans1 == "Y" or ans1 == "y" or ans1 == "Yes" or ans1 == "YES" or ans1 == "yes":
        return loadingScrn() 
    else:
        raise ValueError("Answer does not work")

def firstQuestion(x):
    if x == ("Y", "y", "yes", "YES", "Yes"):
        clear()
        print("\033[0;36mYou put bread in the toaster")
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
        return "Suddenly toast leaps out of the toaster and starts attacking you!!"
    else:
        clear()
        raise ValueError

def question2():
    pass
        
def fightSeq():
    print("\n\n       🍞              ヽ(°□°ヽ)\n   [▇▇▇▇▇▇▇▇]          [▇▇▇▇▇▇▇▇]\n\n")


def firstBattle(x):
        if x == ("Fight", "FIGHT", "fight"):
            clear()
            print("You decide to fight the piece of Toast!")
        elif x == ("RUN", "run", "Run"):
            clear()
            chance = Random.random(0, 100)
            if chance < 50:
                print("You Fail to Escape!")
                return fightSeq()
            else:
                print("You Successfully Escape!")
                return question2()

        else:
            raise ValueError

# Calls

clear()

try:
    print(startGame(input("\033[0;37mDo you want to start the game? \n")))
except:
    clear()
    print(startGame(input("\033[0;37mDo you want to start the game? \n")))

print("You wake up feeling hungry...", end=".")

try:
    print(firstQuestion(input(" Make toast?\n")))
except:
    clear()
    print(firstQuestion(input(" Make toast?\n")))

sleep(0.7)

try:
    firstBattle(input("Do you fight the toast? |FIGHT| |RUN| \n"))
except:
    clear()
    firstBattle(input("Do you fight the toast? |FIGHT| |RUN| \n"))

fightSeq()
