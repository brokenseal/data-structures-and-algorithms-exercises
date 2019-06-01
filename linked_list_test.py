from unittest import TestCase
from linked_list import SinglyLinkedList, Node


class SinglyLinkedTestCase(TestCase):
    def test_initialization(self):
        linked = SinglyLinkedList()

        self.assertIsInstance(linked, SinglyLinkedList)

    def test_append_single(self):
        linked = SinglyLinkedList()
        linked.append(Node(100))

        self.assertValues(linked, [100])

    def test_append_multiple(self):
        linked = SinglyLinkedList()
        linked.append(Node(100))
        linked.append(Node(200))
        linked.append(Node(300))

        self.assertValues(linked, [100, 200, 300])

    def test_append_multiple_with_initial_value(self):
        linked = SinglyLinkedList(Node(1000))
        linked.append(Node(100))
        linked.append(Node(200))
        linked.append(Node(300))

        self.assertValues(linked, [1000, 100, 200, 300])

    def test_insert(self):
        linked = SinglyLinkedList(Node(100))
        linked.append(Node(200))
        linked.append(Node(300))
        linked.insert(Node(1000), 2)

        self.assertValues(linked, [100, 200, 1000, 300])

    def test_insert_at_the_beginning_with_initial_value(self):
        linked = SinglyLinkedList(Node(100))
        linked.insert(Node(1000), 0)

        self.assertValues(linked, [1000, 100])

    def test_insert_at_the_beginning_without_initial_value(self):
        linked = SinglyLinkedList()
        linked.insert(Node(1000), 0)

        self.assertValues(linked, [1000])

    def test_insert_at_the_end(self):
        linked = SinglyLinkedList(Node(100))
        linked.append(Node(200))
        linked.append(Node(300))
        linked.insert(Node(1000), 2)

        self.assertValues(linked, [100, 200, 1000, 300])

    def test_insert_in_the_middle(self):
        linked = SinglyLinkedList(Node(100))
        linked.append(Node(200))
        linked.append(Node(300))
        linked.insert(Node(1000), 1)

        self.assertValues(linked, [100, 1000, 200, 300])

    def test_insert_raises_if_index_is_too_big(self):
        linked = SinglyLinkedList(Node(100))

        with self.assertRaises(ValueError):
            linked.insert(Node(1000), 1)

    def test_remove(self):
        linked = SinglyLinkedList(Node(100))
        linked.append(Node(200))
        linked.append(Node(300))
        linked.remove(1)

        self.assertValues(linked, [100, 300])

    def test_remove_at_the_beginning(self):
        linked = SinglyLinkedList(Node(100))
        linked.remove(0)

        self.assertValues(linked, [])

    def test_remove_at_the_end(self):
        linked = SinglyLinkedList(Node(100))
        linked.append(Node(200))
        linked.append(Node(300))
        linked.append(Node(400))
        linked.append(Node(500))
        linked.remove(4)

        self.assertValues(linked, [100, 200, 300, 400])

    def test_remove_raises_if_index_is_too_big(self):
        linked = SinglyLinkedList(Node(100))

        with self.assertRaises(ValueError):
            linked.remove(4)

    def test_remove_raises_if_index_is_too_small(self):
        linked = SinglyLinkedList()

        with self.assertRaises(ValueError):
            linked.remove(0)

    def assertValues(self, linked, values):
        self.assertEqual(linked.as_list_of_values(), values)


class TestUtilitiesMethods(TestCase):
    def test_as_list_of_values(self):
        linked = SinglyLinkedList()
        linked.append(Node(100))
        linked.append(Node(200))
        linked.append(Node(300))

        self.assertEqual(linked.as_list_of_values(), [100, 200, 300])

    def test_as_list_of_values_no_data(self):
        linked = SinglyLinkedList()

        self.assertEqual(linked.as_list_of_values(), [])

    def test_equality(self):
        self.assertEqual(SinglyLinkedList(), SinglyLinkedList())

    def test_equality_with_values(self):
        first = SinglyLinkedList()
        first.append(Node(100))
        first.append(Node(200))
        first.append(Node(300))
        second = SinglyLinkedList()
        second.append(Node(100))
        second.append(Node(200))
        second.append(Node(300))

        self.assertEqual(first, second)

    def test_inequality_with_values(self):
        first = SinglyLinkedList()
        first.append(Node(100))
        first.append(Node(200))
        first.append(Node(300))
        second = SinglyLinkedList()
        second.append(Node(110))
        second.append(Node(200))
        second.append(Node(300))

        self.assertNotEqual(first, second)

    def test_inequality_with_different_nodes(self):
        first = SinglyLinkedList()
        first.append(Node(100))
        second = SinglyLinkedList()
        second.append(Node(100))
        second.append(Node(200))
        second.append(Node(300))

        self.assertNotEqual(first, second)
