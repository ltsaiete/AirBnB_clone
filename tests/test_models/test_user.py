import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    def test_id(self):
        user = User()
        user2 = User()
        self.assertTrue(isinstance(user.id, str))
        self.assertNotEqual(user.id, user2.id)

    def test_created_at(self):
        user = User()
        now = datetime.now()
        self.assertAlmostEqual(user.created_at, now)

    def test_updated_at(self):
        user = User()
        now = datetime.now()
        self.assertAlmostEqual(user.updated_at, now)
