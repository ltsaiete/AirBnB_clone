import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    def test_id(self):
        city = City()
        city2 = City()
        self.assertTrue(isinstance(city.id, str))
        self.assertNotEqual(city.id, city2.id)

    def test_created_at(self):
        city = City()
        now = datetime.now()
        self.assertAlmostEqual(city.created_at, now)

    def test_updated_at(self):
        city = City()
        now = datetime.now()
        self.assertAlmostEqual(city.updated_at, now)
