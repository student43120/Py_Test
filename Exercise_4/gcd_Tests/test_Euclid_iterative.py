import unittest

from gcd import Euclid_iterative

class TestGCDIterative(unittest.TestCase):

    def test_Euclid_iterative(self):
        self.assertEqual(Euclid_iterative(48, 18), 6)
        self.assertEqual(Euclid_iterative(56, 48), 8)
        self.assertEqual(Euclid_iterative(17, 5), 1)
        self.assertEqual(Euclid_iterative(30, 45), 15)

if __name__ == '__main__':
    unittest.main()
