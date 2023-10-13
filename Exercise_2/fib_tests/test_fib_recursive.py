import unittest

from fibonacci import recursive_fib

class TestFibonacciRecursive(unittest.TestCase):


    def test_fib_recursive(self):
        self.assertEqual(fib_recursive(0), 0)
        self.assertEqual(fib_recursive(1), 1)
        self.assertEqual(fib_recursive(2), 1)
        self.assertEqual(fib_recursive(3), 2)
        self.assertEqual(fib_recursive(4), 3)
        self.assertEqual(fib_recursive(5), 5)
        self.assertEqual(fib_recursive(10), 55)
        self.assertEqual(fib_recursive(20), 6765)
        self.assertEqual(fib_recursive(30), 832040)

if __name__ == '__main__':
    unittest.main()
