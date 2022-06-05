import unittest

from classes.coat import Coat

class TestCoat(unittest.TestCase):
    def setUp(self):
        self.coat1 = Coat("Dinner jacket")


    def test_coat_has_name(self):
        self.assertEqual("Dinner jacket", self.coat1.name)
