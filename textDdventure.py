import os
from os import *
import time
from time import *
import threading
from threading import *
import random
from random import *
# Variables

pHP = 100
toastHP = 50

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
<<<<<<< HEAD
    if ans1.lower == 'yes':
=======
    if ans1 == "y" or "yes" or "Yes" or "Y" or "YES":
>>>>>>> d66f0f96f856567d7800da99442b9e42bd7b705a
        return loadingScrn()
    else:
        raise ValueError

def firstQuestion(x):
    if x == "Y" or "y" or "yes" or "YES" or "Yes":
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
<<<<<<< HEAD
        return "Suddenly toast leaps out of the toaster and starts attacking you!!"
    else:
        clear()
        raise ValueError

def question2():
    pass
        
def fightSeq():
    print("\n\n       🍞              ヽ(°□°ヽ)\n   [▇▇▇▇▇▇▇▇]          [▇▇▇▇▇▇▇▇]\n\n")

=======
        return "Suddenly toast leaps out of the toaster and starts attacking you!"
>>>>>>> d66f0f96f856567d7800da99442b9e42bd7b705a

def firstBattle(x):
        if x == "FIGHT" or "Fight" or "fight":
            clear()
<<<<<<< HEAD
            print("You decide to fight the piece of Toast!")
        elif x == "RUN" or "run" or "Run":
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
=======
            print("You decide to fight the piece of Toast")
        elif x == "RUN" or "run" or "Run":
            clear()
            print("You attempt to run")
        else:
            raise ValueError
        
        
        
>>>>>>> d66f0f96f856567d7800da99442b9e42bd7b705a

# Calls

clear()

print("\033[0;31m\n \n        WARNING: Game is case sensitive, all answers should match given prompt.")

sleep(5)

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
<<<<<<< HEAD
    firstBattle(input("Do you fight the toast? |FIGHT| |RUN| \n"))

fightSeq()
=======
    firstBattle(input("Do you fight the toast? |FIGHT| |RUN| \n"))
>>>>>>> d66f0f96f856567d7800da99442b9e42bd7b705a
