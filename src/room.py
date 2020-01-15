# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    '''Room class to store information about each room.'''

    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if not items:
            self.items = []
        else:
            self.items = items

    def __repr__(self):
        return f"Room({self.name}, {self.description}, {self.items})"

    def __str__(self):
        return self.name

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
