from unittest import TestCase, main
from sorting_algorithms import bubble_sort, selection_sort, quick_sort


class BubbleSortTestCase(TestCase):
    def test_1(self):
        self.assertEqual(
            bubble_sort([32, 3, 5, 1, 23, 2]),
            [1, 2, 3, 5, 23, 32]
        )

    def test_2(self):
        self.assertEqual(
            bubble_sort([1, 4, 2, 7, 9, 3]),
            [1, 2, 3, 4, 7, 9]
        )


class SelectionSortTestCase(TestCase):
    def test_1(self):
        self.assertEqual(
            selection_sort([32, 3, 5, 1, 23, 2]),
            [1, 2, 3, 5, 23, 32]
        )

    def test_2(self):
        self.assertEqual(
            selection_sort([1, 4, 2, 7, 9, 3]),
            [1, 2, 3, 4, 7, 9]
        )


class QuickSortTestCase(TestCase):
    def test_1(self):
        self.assertEqual(
            quick_sort([32, 3, 5, 1, 23, 2]),
            [1, 2, 3, 5, 23, 32]
        )

    def test_2(self):
        self.assertEqual(
            quick_sort([1, 4, 2, 7, 9, 3]),
            [1, 2, 3, 4, 7, 9]
        )


if __name__ == "__main__":
    main()
