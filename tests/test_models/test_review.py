import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    def test_id(self):
        review = Review()
        review2 = Review()
        self.assertTrue(isinstance(review.id, str))
        self.assertNotEqual(review.id, review2.id)

    def test_created_at(self):
        review = Review()
        now = datetime.now()
        self.assertAlmostEqual(review.created_at, now)

    def test_updated_at(self):
        review = Review()
        now = datetime.now()
        self.assertAlmostEqual(review.updated_at, now)
