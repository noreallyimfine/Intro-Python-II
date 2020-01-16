import time

from items import Key, Map, Armor, Treasure, Torch, Coin, Rope
from room import Room
from player import Player

# Declare items
items = {
    'key': Key('Key',
               'The key to open all doors and non-doors.'),
    'map': Map('Map',
               'A guide through the maze, directions to save you.'),
    'armor': Armor('Armor',
                   'Deflect bullets, reject speed.'),
    'treasure': Treasure('Treasure',
                         'All the gold anyone can need.'),
    'torch': Torch('Torch',
                   'A light unto men, a candle in the darkness.'),
    'coin': Coin('Coin', 'A shiny valuable coin.'),
    'rope': Rope('Rope',
                 'Stirdy and thick, you never know when it may come in handy.')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     light=True),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty passages run
north and east.""",
                     [items['map']],
                     light=True),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears ahead of you, falling
the darkness. Ahead to the north, a light flickers in the distance,
but there is no way across the chasm. You feel around and find a dark
passage due west.""",
                     [items['key']]),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west to north.
The smell of gold permeates the air.""",
                     [items['armor']]),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure
chamber! You'll need to use the key to open it.""",
                     [items['treasure'], items['torch']]),

    'trap': Room("Trap Room",
                 """You step into the dark room quickly. Too fast to catch
yourself before you step into a large hole in the ground...""")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].w_to = room['trap']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['trap'].e_to = room['overlook']


# Some functions for readability

# sleep function to text doesn't print too quick
def wait(seconds: int) -> None:
    time.sleep(seconds)


# input move prompt
def input_move():
    return input(
        """
        Choose a direction to move. (N, S, W, E).
        You can pick up an item you see by typing 'get <ITEM>.
        You can drop an item you have by typing 'drop <ITEM>.
        Select 'q' to quit:
        ~~>""").lower().split()[:2]


#
# Main
#
def main():
    # Welcome statement
    print()
    print('\n')
    print("Welcome to Triton's Treasure!")
    print('\n')
    print("Your treasure hunting adventure awaits...")
    print('='*50)
    wait(0.5)

    # Create player with user input, standing 'outside'
    player_name = input("Choose a name: ")
    if player_name != '':
        player = Player(player_name, room['outside'])
    else:
        player = Player('Player1', room['outside'])

    # TEMP
    print(player)

    directions = ['n', 's', 'w', 'e']

    # REPL Loop:
    while True:
        print('='*50)
        # Print players items
        player.inventory()
        wait(1)
        print('='*50)
        # Prints the current room name
        print(f"Standing in the {player.current_room}, you look around.")
        print('\n')
        wait(1)

        # Print the current room description.
        player.current_room.print_description()
        # * Waits for user input and decides what to do.
        # ask for input until they choose an option
        move = input_move()
        # if length of move is 2
        if len(move) == 1:
            move = move[0]
            if move in directions:
                player.travel(move)
            elif move == 'q':
                print(
                    """
        You have given up on your quest for treasure.
                    """)
                break
            else:
                print(
                    """
        That's not a valid choice.
                    """)
        else:
            # Parse first word to pick up to drop and carry out action
            action, item = move
            if action == 'get' or action == 'take':
                player.get_item(items[item])
            elif action == 'drop':
                player.drop_item(items[item])
            # ask for input until its a valid choice
            valid_move = move_is_valid(player, move)
            while not valid_move:
                # ask for input saying cant go that way
                move = input(
                    """
            Can't move in that direction! Select another choice (N, S, W, E):
                    """).lower()
                valid_move = move_is_valid(player, move)

        # Check for win
        if player.current_room == room['treasure']:
            if items['treasure'] in player.current_room.items:
                print("You got the treasure!")
                print("You win!")
                break

        # Line break for clarity
        print()


if __name__ == "__main__":
    main()
