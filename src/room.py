# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_item(self, item):
        self.items.append(item)
        return True
    
    def list_items(self):
        return self.items

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            return False


    def __str__(self):
        return F"Name: {self.name}\nDescription: {self.description}"