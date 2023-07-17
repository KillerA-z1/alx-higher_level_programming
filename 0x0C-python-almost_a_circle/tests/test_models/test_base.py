#!/usr/bin/python3
"""This Module test the Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""
    def setUp(self):
        """Reset the __nb_objects counter before each test case"""
        Base._Base__nb_objects = 0

    def test_CorrectIdOneObjNoId(self):
        """Check if we get the correct id when no id is given"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_CorrectIdTwoObjNoId(self):
        """Check if we get the correct id for a second obj with no id given"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_CorrectIdThreeObjWithId(self):
        """Check if we get the correct id for a third obj with a given id"""
        b1 = Base()
        b2 = Base()
        b3 = Base(13)
        self.assertEqual(13, b3.id)

    def test_create(self):
        """Test the create method"""
        r_dict = {'width': 10, 'height': 7, 'x': 2, 'y': 8, 'id': 9}
        r = Rectangle.create(**r_dict)
        s_dict = {'size': 10, 'x': 1, 'y': 2, 'id': 5}
        s = Square.create(**s_dict)

        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(s, Square)
        self.assertEqual(r.id, 9)
        self.assertEqual(s.id, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_CorrectIdFourObjWithId(self):
        """Check if we get the correct ID for a fourth object with a given ID"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()
