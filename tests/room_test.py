import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.bar import Bar
from classes.coat import Coat

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.room1 = Room("Disco Room", 20, 0, 6)
        self.room2 = Room("Jazz Room", 5, 0, 10)
        self.room3 = Room("Cloak Room", 2, 0, 0)
        self.guest1 = Guest("Boris", 20, "Dancing Queen")
        self.guest2 = Guest("Carrie", 10, "Flamenco Sketches")
        self.guest3 = Guest("Dom", 5, "Just The Two Of Us")
        self.song1 = Song("Dancing Queen")
        self.song2 = Song("Flamenco Sketches")
        self.song3 = Song("Just The Two of Us")
        self.bar1 = Bar("Disco bar", 100)
        self.bar2 = Bar("Jazz Bar", 100)
        self.coat1 = Coat("Dinner jacket")
        self.coat2 = Coat("Poncho")
        self.coat3 = Coat("Hoodie")

    
    def test_room_has_name(self):
        self.assertEqual("Disco Room", self.room1.name)
    
    def test_room_is_empty(self):
        self.assertEqual([], self.room1.occupants)
    
    def test_can_add_customer_to_room(self):
        self.room1.add_occupant(self.guest1)
        self.assertEqual([self.guest1], self.room1.occupants)
    
    def test_no_song_is_playing(self):
        self.assertEqual([], self.room1.now_playing)

    def test_song_is_playing(self):
        self.room1.play_song(self.song1)
        self.assertEqual([self.song1], self.room1.now_playing)

    def test_music_off(self):
        self.room1.play_song(self.song1)
        self.room1.stop_song()
        self.assertEqual([], self.room1.now_playing)

    def test_check_room_for_guest_not_found(self):
        self.assertEqual(False, self.room1.check_room_for_guest(self.guest1))

    def test_check_room_for_guest_found(self):
        self.room1.add_occupant(self.guest1)
        self.assertEqual(True, self.room1.check_room_for_guest(self.guest1))

    def test_get_occupancy(self):
        self.room1.add_occupant(self.guest1)
        self.room1.add_occupant(self.guest2)
        self.assertEqual(2, self.room1.get_occupancy())
    
    def test_add_occupant(self):
        self.room3.add_occupant(self.guest1)
        self.room3.add_occupant(self.guest2)
        self.room3.add_occupant(self.guest3)
        self.assertEqual([self.guest1, self.guest2], self.room3.occupants)
    
    def test_room_has_till(self):
        self.assertEqual(0, self.room1.till)
        self.assertEqual(0, self.room2.till)
        self.assertEqual(0, self.room3.till)
        
    def test_room_has_entry_fee(self):
        self.assertEqual(6, self.room1.entry_fee)
        self.assertEqual(10, self.room2.entry_fee)
        self.assertEqual(0, self.room3.entry_fee)

    def test_can_add_to_till(self):
        self.room1.add_to_till(1)
        self.room2.add_to_till(2)
        self.room3.add_to_till(3)
        self.assertEqual(1, self.room1.till)
        self.assertEqual(2, self.room2.till)
        self.assertEqual(3, self.room3.till)

    def test_admit_to_room_pass(self):
        self.room1.admit_to_room(self.guest1)
        self.assertEqual([self.guest1], self.room1.occupants)
        self.assertEqual(6, self.room1.till)
        self.assertEqual(14, self.guest1.wallet)

    def test_admit_to_room_fail_room_full(self):
        self.room3.admit_to_room(self.guest1)
        self.room3.admit_to_room(self.guest2)
        self.room3.admit_to_room(self.guest3)
        self.assertEqual([self.guest1, self.guest2], self.room3.occupants)

    def test_admit_to_room_fail_room_to_expensive(self):
        self.room2.admit_to_room(self.guest3)
        self.assertEqual([], self.room2.occupants)
        
    def test_favourite_song_is_playing_true(self):
        self.room1.play_song(self.song1)
        self.room1.admit_to_room(self.guest1)
        self.assertEqual("What a banger!", self.room1.is_rowdy(self.guest1))

    def test_favourite_song_is_playing_false(self):
        self.room1.play_song(self.song1)
        self.room1.admit_to_room(self.guest2)
        self.assertEqual(None, self.room1.is_rowdy(self.guest2))

    def test_can_remove_from_room_guest_in_room(self):
        self.room1.admit_to_room(self.guest1)
        self.room1.remove_occupant(self.guest1)
        self.assertEqual([], self.room1.occupants)

    def test_can_remove_from_room_guest_not_in_room(self):
        self.room1.admit_to_room(self.guest2)
        self.room1.remove_occupant(self.guest1)
        self.assertEqual([self.guest2], self.room1.occupants)

    def test_room_has_bar_no_bar(self):
        self.assertEqual([], self.room1.bar)
        self.assertEqual([], self.room2.bar)

    def test_room_has_bar(self):
        self.room1.open_bar(self.bar1)
        self.room2.open_bar(self.bar2)
        self.assertEqual([self.bar1], self.room1.bar)
        self.assertEqual([self.bar2], self.room2.bar)

    def test_can_add_coat_to_coat_rack(self):
        self.room3.add_to_coat_rack(self.coat1)
        self.assertEqual([self.coat1], self.room3.coat_rack)

    def test_can_remove_caot_from_rack(self):
        self.room3.add_to_coat_rack(self.coat1)
        self.room3.remove_from_coat_rack(0)
        self.assertEqual([], self.room3.coat_rack)
    
    def test_can_give_reciept_for_coat(self):
        self.room3.return_reciept(self.coat1, self.guest1)
        self.assertEqual([self.coat1], self.room3.coat_rack)
        self.assertEqual(1, self.guest1.reciept)
    
    def test_can_give_coat_back_to_customer(self):
        self.guest1.add_coat(self.coat1)
        self.assertEqual([self.coat1], self.guest1.coat)
        self.assertEqual(0, self.guest1.reciept)
        self.assertEqual([], self.room3.coat_rack)