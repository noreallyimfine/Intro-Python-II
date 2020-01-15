import textwrap

from items import Key, Map, Armor, Treasure
from room import Room
from player import Player

# Declare items
items = {
    'masterkey': Key('MasterKey',
                     'The key to open all doors and non-doors.'),
    'mainmap': Map('MainMap',
                   'A guide through the maze, directions to save you.'),
    'austerearmor': Armor('AustereArmor',
                          'Deflect bullets, reject speed.'),
    'tritontreasure': Treasure('TritonTreasure',
                               'All the gold anyone can need.')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['mainmap']]),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the
                    darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm.""",
                     [items['masterkey']]),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west to north.
                     The smell of gold permeates the air.""",
                     [items['austerearmor']]),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure
                     chamber! Sadly, it has already been completely emptied by
                     earlier adventurers. The only exit is to the south.""",
                     [items['tritontreasure']]),
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

# Some functions for readability


# input move prompt
def input_move():
    return input(
        """
           Choose a direction to move. (N, S, W, E).
           You can pick up an item you see by typing 'get <ITEM>.
           You can drop an item you have by typing 'drop <ITEM>.
           Select 'q' to quit: """).lower().split()


# execute directional move
def directonal_move(player: Player, move: str) -> None:
    if move == 'n':
        player.current_room = player.current_room.n_to
        print("You went North.")
    elif move == 's':
        player.current_room = player.current_room.s_to
        print("You went South.")
    elif move == 'w':
        player.current_room = player.current_room.w_to
        print("You went West.")
    elif move == 'e':
        player.current_room = player.current_room.e_to
        print("You went East.")


# attempt to pick up item
def add_item(player: Player, item: str) -> None:
    if items[item] in player.current_room.items:
        player.get_item(item)
        print(f"You picked up {item}")
        print(f"You are now holding {player.items}")

    else:
        print(f'The {item} is nowhere is sight!')


# attempt to drop item
def drop_item(player: Player, item: str) -> None:
    if items[item] in player.items.name:
        player.drop_item(item)
        player.current_room.items.append(item)
        print(f"You dropped {item}")
        print(f"You are now holding {player.items}")
    else:
        print("Can't drop an item we don't have!")


#
# Main
#
def main():
    # Create new player object that is currently in the 'outside' room.
    player = Player('Player1', room['outside'])
    player_name = input("Choose a name: ")
    if player_name != '':
        player.name = player_name
    print(player)
    # REPL Loop:
    while True:
        # Prints the current room name
        print("Standing in the", player.current_room, "you look around")
        print('*'*50)
        # Prints the current description.
        text = textwrap.wrap(player.current_room.description, width=50)
        print('\n'.join(text))
        print('*'*50)
        # Print items in room
        print("In the dim light, you see", player.current_room.items)
        # * Waits for user input and decides what to do.
        # ask for input until they choose an option
        move = input_move()
        # if length of move is 2
        if len(move) == 2:
            # Parse first word to pick up to drop and carry out action
            action, item = move
            if action == 'get':
                add_item(player, item)
                move = input_move()
            elif action == 'drop':
                drop_item(player, item)
                move = input_move()
        # only one word typed -> its a directional move
        else:
            # its a directional move
            move = move[0]
            options = 'nwseq'
            while move not in options:
                # ask for input saying not a valid choice
                move = input(
                    """
            That's not a valid choice. Please select a cardinal directions
            (N, S, W, E):
                    """).lower()

            # if the move is q, print and quit
            if move == 'q':
                print("You have given up on your quest for treasure.")
                break

            # ask for input until its a valid choice
            valid_move = hasattr(player.current_room, f'{move}_to')
            while not valid_move:
                # ask for input saying cant go that way
                move = input(
                    """
            Can't move in that direction! Select another choice (N, S, W, E):
                    """).lower()
                valid_move = hasattr(player.current_room, f'{move}_to')

            # carry out move
            directonal_move(player, move)
        # Line break for clarity
        print()


if __name__ == "__main__":
    main()
