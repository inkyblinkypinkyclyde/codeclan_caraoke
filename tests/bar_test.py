import unittest


import unittest

from classes.bar import Bar
from classes.guest import Guest

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar1 = Bar("Disco Bar", 100)
        self.guest1 = Guest("Boris", 20, "Dancing Queen")
        self.guest2 = Guest("Carrie", 10, "Flamenco Sketches")
        self.guest3 = Guest("Dom", 5, "Just The Two Of Us")

    def test_bar_has_name(self):
        self.assertEqual("Disco Bar", self.bar1.name)
    
    def test_bar_has_till(self):
        self.assertEqual(100, self.bar1.till)
    
    def test_remove_cash(self):
        self.bar1.subtract_cash(10)
        self.assertEqual(90, self.bar1.till)
    
    def test_add_cash(self):
        self.bar1.add_cash(10)
        self.assertEqual(110, self.bar1.till)

    def test_can_check_stock(self):
        self.assertEqual(0, self.bar1.stock["Creme De Menthe"]["qty"])
        self.assertEqual(0, self.bar1.stock["Appletini"]["qty"])
        self.assertEqual(0, self.bar1.stock["Water"]["qty"])

    def test_can_add_drink_to_stock(self):
        self.bar1.add_drink("Creme De Menthe", 1)
        self.bar1.add_drink("Appletini", 2)
        self.bar1.add_drink("Water", 3)
        self.assertEqual(1, self.bar1.stock["Creme De Menthe"]["qty"])
        self.assertEqual(2, self.bar1.stock["Appletini"]["qty"])
        self.assertEqual(3, self.bar1.stock["Water"]["qty"])

    def test_can_remove_drink(self):
        self.bar1.add_drink("Creme De Menthe", 1)
        self.bar1.add_drink("Appletini", 2)
        self.bar1.add_drink("Water", 3)
        self.bar1.remove_drink("Creme De Menthe", 1)
        self.bar1.remove_drink("Appletini", 2)
        self.bar1.remove_drink("Water", 3)
        self.assertEqual(0, self.bar1.stock["Creme De Menthe"]["qty"])
        self.assertEqual(0, self.bar1.stock["Appletini"]["qty"])
        self.assertEqual(0, self.bar1.stock["Water"]["qty"])

    def test_can_sell_drink(self):
        self.bar1.add_drink("Creme De Menthe", 1)
        self.bar1.add_drink("Appletini", 2)
        self.bar1.add_drink("Water", 3)
        self.bar1.sell_drink("Appletini", self.guest1, 1)
        self.assertEqual(1, self.bar1.stock["Creme De Menthe"]["qty"])
        self.assertEqual(1, self.bar1.stock["Appletini"]["qty"])
        self.assertEqual(3, self.bar1.stock["Water"]["qty"])
        self.assertEqual(10, self.guest1.wallet)

    def test_can_not_sell_drink_no_stock(self):
        self.bar1.add_drink("Creme De Menthe", 1)
        self.bar1.add_drink("Appletini", 2)
        self.bar1.add_drink("Water", 3)
        self.bar1.sell_drink("Appletini", self.guest1, 3)
        self.assertEqual(1, self.bar1.stock["Creme De Menthe"]["qty"])
        self.assertEqual(2, self.bar1.stock["Appletini"]["qty"])
        self.assertEqual(3, self.bar1.stock["Water"]["qty"])
        self.assertEqual(20, self.guest1.wallet)

    def test_can_not_sell_drink_too_expensive(self):
        self.bar1.add_drink("Creme De Menthe", 1)
        self.bar1.add_drink("Appletini", 2)
        self.bar1.add_drink("Water", 3)
        self.bar1.sell_drink("Creme De Menthe", self.guest1, 1)
        self.assertEqual(1, self.bar1.stock["Creme De Menthe"]["qty"])
        self.assertEqual(2, self.bar1.stock["Appletini"]["qty"])
        self.assertEqual(3, self.bar1.stock["Water"]["qty"])
        self.assertEqual(20, self.guest1.wallet)





