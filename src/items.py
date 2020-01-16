"""Create a item class as base class for items"""


class Item:
    '''Base item class for creating items'''
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

    def on_take(self):
        print(f"You picked up {self.name}")

    def on_drop(self):
        print(f"You dropped {self.name}")


class Key(Item):
    '''Key item for opening treasure chest.'''
    def __init__(self, name, description):
        super().__init__(name, description)


class Map(Item):
    '''Map for seeing the whole area'''
    def __init__(self, name, description):
        super().__init__(name, description)


class Armor(Item):
    '''Armor to increase damage resistance.'''
    def __init__(self, name, description):
        super().__init__(name, description)


class Treasure(Item):
    '''What you came looking for.'''
    def __init__(self, name, description):
        super().__init__(name, description)


class Torch(Item):
    '''To see in the dark.'''
    def __init__(self, name, description):
        super().__init__(name, description)


class Coin(Item):
    '''Money for bribing.'''
    def __init__(self, name, description):
        super().__init__(name, description)


class Rope(Item):
    '''A safety rope, an be used once and discarded.'''
    def __init__(self, name, description):
        super().__init__(name, description)
