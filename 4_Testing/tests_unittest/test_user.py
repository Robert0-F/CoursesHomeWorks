import unittest
import user


class TestUser(unittest.TestCase):
    def setUp(self):
        self.obj = user.User()

    def tearDown(self):
        pass

    def test_init(self):
        obj1 = user.User('Obj', 25)
        assert obj1.name =='Obj'
        self.assertEqual(obj1.age, 25)


        self.assertEqual(self.obj.name, 'Bot')
        self.assertEqual(self.obj.age, 10)

    def test_set_hobbies(self):
        obj = user.User()
        obj.set_hobbies('skate,football')
        assert type(obj.hobbies) is list
        assert len(obj.hobbies) == 2
        assert obj.hobbies[0] == 'skate'
