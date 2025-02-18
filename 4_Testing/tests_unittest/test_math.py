import unittest
import main

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)
        self.assertEqual(main.add(), 0)


