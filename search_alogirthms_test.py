from unittest import TestCase, main, skip
from search_algorithms import binary_search


class BinarySearchTestCase(TestCase):
    def test_simple_case(self):
        result = binary_search([4, 23, 32, 53, 54, 100, 92, 219, 392], 53)

        self.assertEqual(result, 3)

    def test_value_in_the_middle(self):
        result = binary_search([4, 23, 32, 53, 54, 100, 92, 219, 392], 54)

        self.assertEqual(result, 4)

    def test_highest_iteration_right_first(self):
        result = binary_search([4, 23, 32, 53, 54, 100, 92, 219, 392], 92)

        self.assertEqual(result, 6)

    def test_highest_iteration_left_first(self):
        result = binary_search([4, 23, 32, 53, 54, 100, 92, 219, 392], 4)

        self.assertEqual(result, 0)

    def test_no_result(self):
        result = binary_search([4, 23, 32, 53, 54, 100, 92, 219, 392], 414)

        self.assertEqual(result, -1)


if __name__ == "__main__":
    main()
