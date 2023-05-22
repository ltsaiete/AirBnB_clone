import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_id(self):
        amenity = Amenity()
        amenity2 = Amenity()
        self.assertTrue(isinstance(amenity.id, str))
        self.assertNotEqual(amenity.id, amenity2.id)

    def test_created_at(self):
        amenity = Amenity()
        now = datetime.now()
        self.assertAlmostEqual(amenity.created_at, now)

    def test_updated_at(self):
        amenity = Amenity()
        now = datetime.now()
        self.assertAlmostEqual(amenity.updated_at, now)
