# Python Text RPG

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


# Player Set up
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start' 

my_player = player()

# Title Screen Selections
def title_screen_seclections():
    #Ask for player input and execute related functions
    option = input("> ")

    if option.lower() == ("enter"):
        start_game()#placeholder

    elif option.lower() == ("help"):
        help_menu()

    elif option.lower() == ("quit"):
        sys.exit()

    #Check player input and reset menu if wrong input
    while option.lower() not in ['enter', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")

        if option.lower() == ("enter"):
            start_game()#placeholder

        elif option.lower() == ("help"):
            help_menu()

        elif option.lower() == ("quit"):
            sys.exit()

#UI Title Screen
def title_screen():
    os.system('clear')
    print('#############################')
    print('##WELCOME TO THE TEXT NET!###')
    print('#############################')
    print('----------- ENTER------------')
    print('----------- HELP-------------')
    print('----------- QUIT-------------')
    print('#############################')
    print('#############################')
    title_screen_seclections()

#Help Menu
def help_menu():
    print('#################################')
    print('##WELCOME TO THE TEXT NET!#######')
    print('#################################')
    print('USE UP, DOWN, LEFT, RIGHT TO MOVE')
    print('TYPE COMMANDS TO DO THEM#########')
    print('#ENJOY YOUR TIME IN THE TEXT NET#')
    print('#################################')
    print('#################################')
    title_screen_seclections()






##MAP##
#    A1  A2  A3  A4
#   ----------------
# B1|   |   |   |  | 
#   ----------------
# C1|   |   |   |  |
#   ---------------- 
# D1|   |   |   |  |
#   ----------------
# E1|   |   |   |  |
#   ----------------

#PLAYER STARTS AT B2
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION ='examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False,'a2': False,'a3': False,'a4': False,
                'b1': False,'b2': False,'b3': False,'b4': False,
                'c1': False,'c2': False,'c3': False,'c4': False, 
                'd1': False,'d2': False,'d3': False,'d4': False,
                'e1': False,'e2': False,'e3': False,'e4': False,
                }


zonemap = {
    ################################TOWN##################################
    'a1': {
        ZONENAME: "City Hall",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'a2': {
        ZONENAME: "City Market",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'a3': {
        ZONENAME: "City Council",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'a4': {
        ZONENAME: "City Arena",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },


    #############   ADEVENTURE AREA   ############ 
    'b1': {
        ZONENAME: "Forbidden Jungle",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'b2': {
        ZONENAME: "Your Home",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'b3': {
        ZONENAME: "Old City Ruins",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'b4': {
        ZONENAME: "The Bog",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

######    DESERT AREA   ############
    'c1': {
        ZONENAME: "Digital Desert",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'c2': {
        ZONENAME: "Skull Canyon",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'c3': {
        ZONENAME: "Spider Caves",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'up',
        DOWN : 'down',
        LEFT : 'left',
        RIGHT : 'right'
    },

    'c4': {
        ZONENAME: "Snowy Volcanoe",
        DESCRIPTION :  'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b4',
        DOWN : 'd4',
        LEFT : 'c3',
        RIGHT : 'c5'
    },
}

####### GAME INTERACTIVITY ###################
def print_location():
    print('\n' + ('#' * (4 + len(my_player.location))))
    print('#' + my_player.location.upper() + ' #')
    print('#' + zonemap[my_player.position][DESCRIPTION] + '#')
    print('\n' + ('#' * (4 + len(my_player.location))))

def prompt():
    print("\n" + "########################")
    print("What are you going to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk']





######### GAME FUNCTIONALITY ##################
def start_game():
    return 

