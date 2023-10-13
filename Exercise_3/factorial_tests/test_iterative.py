import unittest


from factorial import iterative

class TestIterativeFunction(unittest.TestCase):

    def test_iterative(self):
        self.assertEqual(iterative(0), 1)
        self.assertEqual(iterative(1), 1)
        self.assertEqual(iterative(2), 2)
        self.assertEqual(iterative(5), 120)
        self.assertEqual(iterative(10), 3628800)

if __name__ == '__main__':
    unittest.main()
