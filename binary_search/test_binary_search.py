import unittest
from binary_search import binary_search


class BinarySearchTestCase(unittest.TestCase):
    """Tests for binary search."""

    def test_search_for_element(self):
        """
        Tests whether the binary search can find a required element and return
        its correct index.
        """
        list = [1, 2, 3, 4, 5, 8, 9]
        element = 5
        index = binary_search(list, element)
        self.assertEqual(4, index)

    def test_search_for_element_in_single_element_list(self):
        """
        Tests whether the binary search can find a required element in a list
        that is of a single element and return its correct index.
        """
        list = [7]
        element = 7
        index = binary_search(list, element)
        self.assertEqual(0, index)

    def test_search_for_non_existent_element(self):
        """
        Tests whether the binary search correctly returns None in the case of
        the required element not existing.
        """
        list = [1, 2, 3, 4, 5, 8, 9]
        element = 6
        index = binary_search(list, element)
        self.assertEqual(None, index)


if __name__ == '__main__':
    unittest.main()
