# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    '''Player class to hold information about player
       and to be controlled by user.'''

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def travel(self, direction):
        # Move player in direction chosen
        pass

    def get_item(self, item):
        if item in self.current_room.items:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.on_take()
            print(f"You are now holding {self.items}")
        else:
            print(f'The {item} is nowhere is sight!')

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.current_room.items.append(item)
            item.on_drop()
            # print(f"You dropped {item}")
            print(f"You are are now holding {', '.join(self.items)}")
        else:
            print("Can't drop an item we don't have!")

    def i(self):
        for i in self.items:
            print(i)

    def inventory(self):
        item_string = "You are currently holding:\n"
        item_string += '\n'.join([item.name for item in self.items])
        print(item_string)

    def __repr__(self):
        return f"Player({self.name}, {self.current_room})"

    def __str__(self):
        return self.name
