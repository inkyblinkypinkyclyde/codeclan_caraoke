class Room:

    def __init__(self, name, max_occupancy, till, entry_fee):
        self.name = name
        self.max_occupancy = max_occupancy
        self.till = till
        self.entry_fee = entry_fee
        self.occupants = []
        self.now_playing = []
        self.bar = []
        self.coat_rack = []
    
    def add_occupant(self, occupant):
        if len(self.occupants) < self.max_occupancy:
            self.occupants.append(occupant)
    
    def remove_occupant(self, guest):
        if self.check_room_for_guest(guest):
            self.occupants.remove(guest)

    def admit_to_room(self, guest):
        if self.get_occupancy() < self.max_occupancy:
            if guest.wallet >= self.entry_fee:
                self.add_occupant(guest)
                self.add_to_till(self.entry_fee)
                guest.remove_cash(self.entry_fee)
    
    def play_song(self, play_song):
        self.now_playing.append(play_song)
    
    def stop_song(self):
        self.now_playing.clear()
    
    def check_room_for_guest(self, guest):
        for occupant in self.occupants:
            if occupant == guest:
                return True
        return False
    
    def get_occupancy(self):
        return len(self.occupants)
    
    def add_to_till(self, amount):
        self.till += amount
    
    def subtract_from_till(self, amount):
        self.till -= amount
    
    def is_rowdy(self, guest):
        if self.now_playing[0].name == guest.favourite_song:
            return "What a banger!"
        
    def open_bar(self, bar):
        self.bar.append(bar)
    
    def add_to_coat_rack(self, coat):
        self.coat_rack.append(coat)
    
    def remove_from_coat_rack(self, ticket):
        self.coat_rack.pop(ticket)

    def return_reciept(self, coat, guest):
        self.add_to_coat_rack(coat)
        guest.reciept = len(self.coat_rack)