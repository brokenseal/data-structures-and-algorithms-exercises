from unittest import TestCase, main
from search_algorithms import binary_search


class BinarySearchTestCase(TestCase):
    def test_simple_case(self):
        result, iterations_count = binary_search(
            [100, 32, 4, 23, 54, 219, 92, 53, 392], 53)

        self.assertEqual(result, True)
        self.assertEqual(iterations_count, 3)

    def test_value_in_the_middle(self):
        result, iterations_count = binary_search(
            [100, 32, 4, 23, 54, 219, 92, 53, 392], 54)

        self.assertEqual(result, True)
        self.assertEqual(iterations_count, 1)

    def test_highest_iteration_right_first(self):
        result, iterations_count = binary_search(
            [100, 32, 4, 23, 54, 219, 92, 53, 392], 92)

        self.assertEqual(result, True)
        self.assertEqual(iterations_count, 4)

    def test_highest_iteration_left_first(self):
        result, iterations_count = binary_search(
            [100, 32, 4, 23, 54, 219, 92, 53, 392], 4)

        self.assertEqual(result, True)
        self.assertEqual(iterations_count, 4)

    def test_no_result(self):
        result, iterations_count = binary_search(
            [100, 32, 4, 23, 54, 219, 92, 53, 392], 414)

        self.assertEqual(result, False)
        self.assertEqual(iterations_count, 3)


if __name__ == "__main__":
    main()
