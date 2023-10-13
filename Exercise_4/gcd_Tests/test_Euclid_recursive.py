import unittest

from gcd import Euclid_recursive

class TestGCDRecursive(unittest.TestCase):

    def test_Euclid_recursive(self):
        self.assertEqual(Euclid_recursive(48, 18), 6)
        self.assertEqual(Euclid_recursive(56, 48), 8)
        self.assertEqual(Euclid_recursive(17, 5), 1)
        self.assertEqual(Euclid_recursive(30, 45), 15)

if __name__ == '__main__':
    unittest.main()
