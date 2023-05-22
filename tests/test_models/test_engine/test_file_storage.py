import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    pass
    # storage = FileStorage()
    # base = BaseModel()
    # FileStorage.__file_path = 'test_file.json'

    # def testInit(self):
    #     print(FileStorage.__file_path)

    # def testNew(self):
    #     self.assertEqual(FileStorage.__objects, {})
    #     self.storage.new(self.base)
    #     self.assertTrue(
    #         f'BaseModel.{self.base.id}' in FileStorage.__objects)
    #     self.assertEqual(
    #         FileStorage.__objects[f'BaseModel.{self.base.id}'],
    #         self.base)

    # def testSave(self):
    #     self.storage.save()
    #     with open(FileStorage.__file_path, 'r') as file:
    #         obj_dict = '{"BaseModel.{}": {"__class__": "BaseModel", \
    #             "updated_at": "{}", "created_at": "{}", "id": "{}"}}}'.format(
    #             self.base.id, self.base.updated_at.isoformat(),
    #             self.base.created_at.isoformat(), self.id)

    #         self.assertEqual(file.read, obj_dict)

    # def testAll(self):
    #     self.assertEqual(self.storage.all(), FileStorage.__objects)

    # def testReload(self):
    #     FileStorage.__objects = {}
    #     self.storage.reload()

    #     self.assertTrue(
    #         f'BaseModel.{self.base.id}' in FileStorage.__objects)
    #     self.assertEqual(
    #         FileStorage.__objects[f'BaseModel.{self.base.id}'],
    #         self.base)
