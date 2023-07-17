import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test(self):
        var1 = Base()
        self.assertEqual(var1.id, 1)
        self.assertIsInstance(var1, Base)


if __name__ == "__main__":
    unittest.main()
