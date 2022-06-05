class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.coat = []
        self.reciept = 0
    
    def remove_cash(self, amount):
        self.wallet -= amount

    def add_cash(self, amount):
        self.wallet += amount

    def add_coat(self, coat):
        self.coat.append(coat)
    
    def remove_coat(self):
        self.coat.pop(0)