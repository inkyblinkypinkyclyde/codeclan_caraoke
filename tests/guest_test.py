import unittest

from classes.guest import Guest
from classes.coat import Coat

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Boris", 20, "Dancing Queen")
        self.coat1 = Coat("Dinner jacket")

    def test_guest_has_name(self):
        self.assertEqual("Boris", self.guest1.name)
    
    def test_remove_cash(self):
        self.guest1.remove_cash(10)
        self.assertEqual(10, self.guest1.wallet)
    
    def test_has_favourite_song(self):
        self.assertEqual("Dancing Queen", self.guest1.favourite_song)

    def test_can_add_coat(self):
        self.guest1.add_coat(self.coat1)
        self.assertEqual([self.coat1], self.guest1.coat)

    def test_can_remove_coat(self):
        self.guest1.add_coat(self.coat1)
        self.guest1.remove_coat()
        self.assertEqual([], self.guest1.coat)
