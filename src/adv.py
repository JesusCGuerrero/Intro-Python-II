from room import Room
from player import Player
from item import Item
import sys


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """The sound of muffled rain and thunder trails from the south.\nDusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. A putrid smell permeates the tight corridor. You hear a faint scratching sound further ahead."""),

    'treasure': Room("Treasure Chamber", """You stumble into the den of a tall lanky eldritch creature. It quickly grabs hold of you with it's fingers, each one matching the length of your arms. As it draws you closer, everything fades to black."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(
    current_room = room["outside"],
    name = "Bruno Mars"
)

# Items:
item = {
    'lighter': Item("Lighter", "It still has some fluid left. Better than nothing I guess."),
    'survival_knife': Item("Survival Knife", "It will keel."),
    'note1': Item("Bloody Note", "\nA note covered in blood. It doesn't seem that old.\n \n'I don't think it followed me into the cave.\nI ran for what seemed like forever.\nNow to find my way back out.'\n"),
    'note2': Item("Torn Note", "\nA half torn note.\n \n'I don't have much time. It                ~\nand grab the key, then                     ~\nonly way out of the cave.                  ~'\n"),
    'note3': Item("Soggy Note", "\nA soggy note.\n \n'It can't see you in the dark.\nBut then you can't see it either can you?\nGood luck.'\n"),
    'ancient_key': Item("Ancient Key", "An otherworldly key. I wonder what it's for."),
}

# Add Items to Rooms:

room['outside'].addItem(item['note2'])
room['foyer'].addItem(item['lighter'])
room['overlook'].addItem(item['lighter'])

# print(item['note2'])
# print(player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# player_input = input("The sky thunders as it begins to pour. You see an eerie cave entrance to the north. Use the WASD keys to move.")

# if player_input == "r":
#     print(player)
#     input("You pull out a map")

# while player.current_room == room["outside"]:

#     if player_input == "w":
#         player.current_room = room["foyer"]
#         print("You climb through the mouth of the cave, collecting several aged cobwebs on your drenched clothes. ")

#     elif player_input == "a":
#         print("There is nothing of interest to your left. It begins to rain harder.")
    
#     elif player_input == "s":
#         print("There is nothing of interest behind you. It begins to rain harder.")
    
#     elif player_input == "d":
#         print("There is nothing of interest to your right. It begins to rain harder.")

# if player_input == "q":
#     sys.exit()
print(player.name)
print("\nThe sky thunders as it begins to pour.\nYou see an eerie cave entrance straight ahead of you.\nTo view your controls, enter 'C'.\n")
player_input = []

while not player_input == "q":
    player_input =  str(input("What will you do?: "))



    if player_input == 'c':
        print("\nControls:\n'W' = Up\n'A' = Left\n'S' = Down\n'D' = Right\n'Q' = Quit.\n'R' = Check Current Room\n")
    
    elif player_input == 'r':
        print(f"\n{player}\n")

    elif player_input == 'w':
        if player.current_room.n_to != []:
            player.current_room = player.current_room.n_to
            print(f"\nYou enter the {player.current_room.name}.\n{player.current_room.description}\n")
            if player.current_room.items != []:
                print(f"\nYou find a {player.current_room.items[0].name}\n")
        else:
            print("\n There's nothing of interest in that direction.\n")

    elif player_input == 'a':
        if player.current_room.w_to != []:
            player.current_room = player.current_room.w_to
            print(f"\nYou enter the {player.current_room.name}.\n{player.current_room.description}\n")
        else:
            print("\n There's nothing of interest in that direction.\n")

    elif player_input == 's':
        if player.current_room.s_to != []:
            player.current_room = player.current_room.s_to
            print(f"\nYou enter the {player.current_room.name}.\n{player.current_room.description}\n")
        else:
            print("\n There's nothing of interest in that direction.\n")

    elif player_input == 'd':
        if player.current_room.e_to != []:
            player.current_room = player.current_room.e_to
            print(f"\nYou enter the {player.current_room.name}.\n{player.current_room.description}\n")
        else:
            print("\n There's nothing of interest in that direction.\n")


    


