import textwrap

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    '''Room class to store information about each room.'''

    def __init__(self, name, description, items=None, light=False):
        self.name = name
        self.description = description
        self.light = light
        if not items:
            self.items = []
        else:
            self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def is_valid_move(self, move):
        return hasattr(self, f'{move}_to')

    def __repr__(self):
        return f"Room({self.name}, {self.description}, {self.items})"

    def __str__(self):
        return self.name

    def print_description(self):
        if not self.light:
            print("""Too dark to see! Can't tell what's here!
You can only guess where to go next""")
        elif self.light:
            text = textwrap.wrap(self.description, width=50)
            print('\n'.join(text))
            print('\n')
            # Print items in room
            print("In the dim light, you see", self.items)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
