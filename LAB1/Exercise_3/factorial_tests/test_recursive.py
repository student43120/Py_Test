import unittest


from factorial import iterative

class TestRecursiveFunction(unittest.TestCase):

    def test_recursive(self):
        self.assertEqual(recursive(0), 1)
        self.assertEqual(recursive(1), 1)
        self.assertEqual(recursive(2), 2)
        self.assertEqual(recursive(5), 120)
        self.assertEqual(recursive(10), 3628800)

if __name__ == '__main__':
    unittest.main()
