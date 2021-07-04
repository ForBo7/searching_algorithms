import unittest
from linear_search import linear_search


class LinearSearchTestCase(unittest.TestCase):

    def test_search_for_element(self):
        """
        Tests whether the linear search can find a required element and return
        its correct index.
        """
        list = [3, 8, 2, 5, 9, 1, 4]
        element = [9]
        index = linear_search(list, element)
        self.assertEqual(5, index)


if __name__ == '__main__':
    unittest.main()
