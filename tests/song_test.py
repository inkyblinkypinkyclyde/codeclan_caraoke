import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Dancing Queen")


    def test_song_has_name(self):
        self.assertEqual("Dancing Queen", self.song1.name)
