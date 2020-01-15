# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    '''Player class to hold information about player
       and to be controlled by user.'''

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def get_item(self, item):
        self.items.append(item)
        self.current_room.items.remove(item)

    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.items.append(item)

    def __repr__(self):
        return f"Player({self.name}, {self.current_room})"
