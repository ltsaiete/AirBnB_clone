import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    def test_id(self):
        state = State()
        state2 = State()
        self.assertTrue(isinstance(state.id, str))
        self.assertNotEqual(state.id, state2.id)

    def test_created_at(self):
        state = State()
        now = datetime.now()
        self.assertAlmostEqual(state.created_at, now)

    def test_updated_at(self):
        state = State()
        now = datetime.now()
        self.assertAlmostEqual(state.updated_at, now)
