import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_id(self):
        place = Place()
        place2 = Place()
        self.assertTrue(isinstance(place.id, str))
        self.assertNotEqual(place.id, place2.id)

    def test_created_at(self):
        place = Place()
        now = datetime.now()
        self.assertAlmostEqual(place.created_at, now)

    def test_updated_at(self):
        place = Place()
        now = datetime.now()
        self.assertAlmostEqual(place.updated_at, now)
