class Bar:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock = {
            "Creme De Menthe": {
                "price": 50,
                "alc_content": 10,
                "qty": 0
            },
            "Appletini": {
                "price": 10,
                "alc_content": 1,
                "qty": 0
            },
            "Water": {
                "price": 1,
                "alc_content": 0,
                "qty": 0
            }
        }
    
    def add_cash(self, amount):
        self.till += amount

    def subtract_cash(self, amount):
        self.till -= amount 

    def add_drink(self, drink_name, number):
        self.stock[drink_name]["qty"] += number
    
    def remove_drink(self, drink_name, number):
        self.stock[drink_name]["qty"] -= number

    def sell_drink(self, drink_name, guest, number):
        cost_of_drinks = self.stock[drink_name]["price"] * number
        if guest.wallet >= cost_of_drinks:
            if number <= self.stock[drink_name]["qty"]:
                self.remove_drink(drink_name, number)
                self.add_cash(self.stock[drink_name]["price"])
                guest.remove_cash(self.stock[drink_name]["price"])


