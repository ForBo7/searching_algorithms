import unittest
from linear_search import linear_search


class LinearSearchTestCase(unittest.TestCase):

    def test_search_for_element(self):
        """
        Tests whether the linear search can find a required element and return
        its correct index.
        """
        list = [3, 8, 2, 5, 9, 1, 4]
        element = 9
        index = linear_search(list, element)
        self.assertEqual(4, index)

    def test_search_for_element_in_single_element_list(self):
        """
        Tests whether the linear search can find a required element in a list
        that is of a single element and return its correct index.
        """
        list = [7]
        element = 7
        index = linear_search(list, element)
        self.assertEqual(0, index)

    def test_search_for_non_existent_element(self):
        """
        Tests whether the linear search correctly returns None in the case of
        the required element not existing.
        """
        list = [3, 8, 2, 5, 9, 1, 4]
        element = 6
        index = linear_search(list, element)
        self.assertEqual(None, index)


if __name__ == '__main__':
    unittest.main()
