#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_save_to_file_csv(self):
        # Create some objects
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        s1 = Square(9, 10, 11)
        s2 = Square(12, 13, 14)
        
        # Save the objects to CSV
        Rectangle.save_to_file_csv([r1, r2])
        Square.save_to_file_csv([s1, s2])
        
        # Load the objects from CSV
        rectangles = Rectangle.load_from_file_csv()
        squares = Square.load_from_file_csv()
        
        # Assert the loaded objects match the original objects
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].width, r1.width)
        self.assertEqual(rectangles[0].height, r1.height)
        self.assertEqual(rectangles[0].x, r1.x)
        self.assertEqual(rectangles[0].y, r1.y)
        self.assertEqual(rectangles[1].width, r2.width)
        self.assertEqual(rectangles[1].height, r2.height)
        self.assertEqual(rectangles[1].x, r2.x)
        self.assertEqual(rectangles[1].y, r2.y)
        
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].size, s1.size)
        self.assertEqual(squares[0].x, s1.x)
        self.assertEqual(squares[0].y, s1.y)
        self.assertEqual(squares[1].size, s2.size)
        self.assertEqual(squares[1].x, s2.x)
        self.assertEqual(squares[1].y, s2.y)


if __name__ == '__main__':
    unittest.main()
