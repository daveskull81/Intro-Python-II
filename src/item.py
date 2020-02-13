class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(F"You have picked up {self.name}")

    def on_drop(self):
        print(F"You have dropped {self.name}")