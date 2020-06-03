class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def pickUpItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)

    def __str__(self):
        return (f"\nCurrent Room: {self.current_room.name}\nRoom Description: {self.current_room.description}\n")