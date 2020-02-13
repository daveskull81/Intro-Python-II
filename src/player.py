# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def update_room(self, room):
        self.current_room = room

    def add_item(self, item):
        self.inventory.append(item)
        item.on_take()
        return True

    def list_inventory(self):
        print(self.inventory)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            item.on_drop()
            return item
        else:
            return False