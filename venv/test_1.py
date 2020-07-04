import unittest
from hw_4 import distance

class TestDist(unittest.TestCase):

    def test_zero(self):
        d = distance(0,0,0,0)
        self.assertEqual(d,0)

    def test_one(self):
        d = distance(0,0,0,2)
        self.assertEqual(d,1)

if __name__ == "__main__":
    unittest.main()