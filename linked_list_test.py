from unittest import TestCase
from linked_list import SinglyLinkedList, Node, StackedSinglyLinkedList


class SinglyLinkedTestCase(TestCase):
    def test_initialization(self):
        linked = SinglyLinkedList()

        self.assertIsInstance(linked, SinglyLinkedList)

    def test_append_single(self):
        linked = SinglyLinkedList()
        linked.append(100)

        self.assertEqual(linked.as_list(), [100])

    def test_append_multiple(self):
        linked = SinglyLinkedList()
        linked.append(100)
        linked.append(200)
        linked.append(300)

        self.assertEqual(linked.as_list(), [100, 200, 300])

    def test_append_multiple_with_initial_value(self):
        linked = SinglyLinkedList(1000)
        linked.append(100)
        linked.append(200)
        linked.append(300)

        self.assertEqual(linked.as_list(), [1000, 100, 200, 300])

    def test_insert(self):
        linked = SinglyLinkedList(100)
        linked.append(200)
        linked.append(300)
        linked.insert(1000, 2)

        self.assertEqual(linked.as_list(), [100, 200, 1000, 300])

    def test_insert_at_the_beginning_with_initial_value(self):
        linked = SinglyLinkedList(100)
        linked.insert(1000, 0)

        self.assertEqual(linked.as_list(), [1000, 100])

    def test_insert_at_the_beginning_without_initial_value(self):
        linked = SinglyLinkedList()
        linked.insert(1000, 0)

        self.assertEqual(linked.as_list(), [1000])

    def test_insert_at_the_end(self):
        linked = SinglyLinkedList(100)
        linked.append(200)
        linked.append(300)
        linked.insert(1000, 2)

        self.assertEqual(linked.as_list(), [100, 200, 1000, 300])

    def test_insert_in_the_middle(self):
        linked = SinglyLinkedList(100)
        linked.append(200)
        linked.append(300)
        linked.insert(1000, 1)

        self.assertEqual(linked.as_list(), [100, 1000, 200, 300])

    def test_insert_raises_if_index_is_too_big(self):
        linked = SinglyLinkedList(100)

        with self.assertRaises(ValueError):
            linked.insert(1000, 1)

    def test_remove(self):
        linked = SinglyLinkedList(100)
        linked.append(200)
        linked.append(300)
        linked.remove(1)

        self.assertEqual(linked.as_list(), [100, 300])

    def test_remove_at_the_beginning(self):
        linked = SinglyLinkedList(100)
        linked.remove(0)

        self.assertEqual(linked.as_list(), [])

    def test_remove_at_the_beginning_with_multiple_values(self):
        linked = SinglyLinkedList(100)
        linked.append(200)
        linked.append(300)
        linked.append(400)
        linked.remove(0)

        self.assertEqual(linked.as_list(), [200, 300, 400])

    def test_remove_at_the_end(self):
        linked = SinglyLinkedList(100)
        linked.append(200)
        linked.append(300)
        linked.append(400)
        linked.append(500)
        linked.remove(4)

        self.assertEqual(linked.as_list(), [100, 200, 300, 400])

    def test_remove_raises_if_index_is_too_big(self):
        linked = SinglyLinkedList(100)

        with self.assertRaises(ValueError):
            linked.remove(4)

    def test_remove_raises_if_index_is_too_small(self):
        linked = SinglyLinkedList()

        with self.assertRaises(ValueError):
            linked.remove(0)

    def test_prepend_adds_an_element_at_the_beginning(self):
        linked = SinglyLinkedList(100)
        linked.prepend(1000)

        self.assertEqual(linked.as_list(), [1000, 100])

    def test_prepend_adds_an_element_at_the_beginning_even_without_a_first_node(self):
        linked = SinglyLinkedList()
        linked.prepend(1000)

        self.assertEqual(linked.as_list(), [1000])

    def test_direct_access_to_elements(self):
        linked = SinglyLinkedList()
        linked.append(100)

        self.assertEqual(linked[0], 100)

    def test_direct_access_to_elements_empty(self):
        linked = SinglyLinkedList()

        with self.assertRaises(IndexError):
            self.assertEqual(linked[0], None)

    def test_direct_access_to_elements_more_than_one_element(self):
        linked = SinglyLinkedList()
        linked.append(100)
        linked.append(200)
        linked.append(300)
        linked.append(400)

        self.assertEqual(linked[2], 300)

    def test_item_setting_by_index(self):
        linked = SinglyLinkedList()
        linked[0] = 100

        self.assertEqual(linked.as_list(), [100])

    def test_item_setting_by_index_with_a_previous_value(self):
        linked = SinglyLinkedList()
        linked.append(100)
        linked[1] = 200

        self.assertEqual(linked.as_list(), [100, 200])

    def test_item_setting_by_index_raise_error_if_index_too_high(self):
        linked = SinglyLinkedList()

        with self.assertRaises(IndexError):
            linked[10] = 200

    def test_item_setting_by_index_overrides_previous_value(self):
        linked = SinglyLinkedList()
        linked.append(100)
        linked.append(200)
        linked.append(300)
        linked[1] = 400

        self.assertEqual(linked.as_list(), [100, 400, 300])

    def test_item_setting_by_index_overrides_previous_value_at_the_beginning(self):
        linked = SinglyLinkedList()
        linked.append(100)
        linked.append(200)
        linked.append(300)
        linked[0] = 400

        self.assertEqual(linked.as_list(), [400, 200, 300])

    def test_item_setting_by_index_overrides_previous_value_at_the_end(self):
        linked = SinglyLinkedList()
        linked.append(100)
        linked.append(200)
        linked.append(300)
        linked[2] = 400

        self.assertEqual(linked.as_list(), [100, 200, 400])


class TestStackedSinglyLinkedList(TestCase):
    def test_push_adds_as_first_node(self):
        linked = StackedSinglyLinkedList(100)
        linked.push(200)

        self.assertEqual(linked.as_list(), [200, 100])

    def test_push_adds_as_first_node_with_multiple_values(self):
        linked = StackedSinglyLinkedList(100)
        linked.push(200)
        linked.push(300)
        linked.push(400)

        self.assertEqual(linked.as_list(), [400, 300, 200, 100])

    def test_pop_removes_first_node(self):
        linked = StackedSinglyLinkedList(100)
        linked.pop()

        self.assertEqual(linked.as_list(), [])

    def test_pop_removes_first_node_with_multiple_nodes(self):
        linked = StackedSinglyLinkedList(100)
        linked.push(200)
        linked.push(300)
        linked.push(400)
        linked.pop()

        self.assertEqual(linked.as_list(), [300, 200, 100])


class TestUtilitiesMethods(TestCase):
    def test_as_list(self):
        linked = SinglyLinkedList()
        linked.append(100)
        linked.append(200)
        linked.append(300)

        self.assertEqual(linked.as_list(), [100, 200, 300])

    def test_as_list_no_data(self):
        linked = SinglyLinkedList()

        self.assertEqual(linked.as_list(), [])

    def test_equality(self):
        self.assertEqual(SinglyLinkedList(), SinglyLinkedList())

    def test_equality_with_values(self):
        first = SinglyLinkedList()
        first.append(100)
        first.append(200)
        first.append(300)
        second = SinglyLinkedList()
        second.append(100)
        second.append(200)
        second.append(300)

        self.assertEqual(first, second)

    def test_inequality_with_values(self):
        first = SinglyLinkedList()
        first.append(100)
        first.append(200)
        first.append(300)
        second = SinglyLinkedList()
        second.append(110)
        second.append(200)
        second.append(300)

        self.assertNotEqual(first, second)

    def test_inequality_with_different_nodes(self):
        first = SinglyLinkedList()
        first.append(100)
        second = SinglyLinkedList()
        second.append(100)
        second.append(200)
        second.append(300)

        self.assertNotEqual(first, second)
