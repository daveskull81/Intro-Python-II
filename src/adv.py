from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

def adventure_game():

    print('\nWelcome to Adventure Game!\n')

    player = Player(input('What is your name? '), room['outside'])

    print(F"\nHello, {player.name}! Adventure forth at your own peril!\n")

    print(F"You can currently be found:\n\n{player.current_room}\n")
    print("\nMake your selections and explore!\n\n")

    while True:
        direction = input("[n] North  [s] South   [e] East    [w] West [q] Quit\n")

        if direction.lower() == 'n':
            if player.current_room.n_to:
                player.update_room(player.current_room.n_to)
                print(F"You now can be found:\n\n{player.current_room}\n")
            else:
                print("\nThere is no room there. Try another direction\n")

        elif direction.lower() == 's':
            if player.current_room.s_to:
                player.update_room(player.current_room.s_to)
                print(F"You now can be found:\n\n{player.current_room}\n")
            else:
                print("\nThere is no room there. Try another direction\n")

        elif direction.lower() == 'e':
            if player.current_room.e_to:
                player.update_room(player.current_room.e_to)
                print(F"You now can be found:\n\n{player.current_room}\n")
            else:
                print("\nThere is no room there. Try another direction\n")

        elif direction.lower() == 'w':
            if player.current_room.w_to:
                player.update_room(player.current_room.w_to)
                print(F"You now can be found:\n\n{player.current_room}\n")
            else:
                print("\nThere is no room there. Try another direction\n")

        elif direction.lower() == 'q':
            print('Thanks for playing!')
            exit()
        else:
            print('\nInvalid choice. Make sure to choose the letter for the direction you wish to travel.\n')

if __name__ == '__main__':
    adventure_game()
# Make a new player object that is currently in the 'outside' room.
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
