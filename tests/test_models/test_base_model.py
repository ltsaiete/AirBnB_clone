import unittest
import uuid
import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id(self):
        base = BaseModel()
        base2 = BaseModel()
        self.assertTrue(isinstance(base.id, str))
        self.assertNotEqual(base.id, base2.id)

    def test_created_at(self):
        base = BaseModel()
        now = datetime.now()
        self.assertAlmostEqual(base.created_at, now)

    def test_updated_at(self):
        base = BaseModel()
        now = datetime.now()
        self.assertAlmostEqual(base.updated_at, now)

    def test_str(self):
        base = BaseModel()
        test_str = f'[BaseModel] ({base.id}) <{base.__dict__}>'
        self.assertEqual(str(base), test_str)

    def test_save_updates_date(self):
        base = BaseModel()
        initialUpdatedAt = base.updated_at
        time.sleep(1)
        base.save()
        self.assertNotEqual(base.updated_at, initialUpdatedAt)

    def testConvertToDict(self):
        base = BaseModel()
        self.assertEqual(base.to_dict(), {
            'id': f'{base.id}',
            '__class__': 'BaseModel',
            'updated_at': f'{base.updated_at.isoformat()}',
            'created_at': f'{base.created_at.isoformat()}',
        })

    def testInstantiationKwargs(self):
        kwargs = {
            'id': str(uuid.uuid4()),
            'created_at': str(datetime.now()),
            'updated_at': str(datetime.now()),
            '__class__': 'BaseModel'
        }
        base = BaseModel(**kwargs)
        self.assertEqual(base.id, kwargs['id'])
        self.assertEqual(
            base.created_at, datetime.fromisoformat(kwargs['created_at']))
        self.assertEqual(
            base.updated_at, datetime.fromisoformat(kwargs['updated_at']))
        self.assertNotEqual(base.__class__, 'BaseModel')
