from unittest import TestCase
from doubly_linked_list import DoublyLinkedList, Node


def get_simple_instance():
    return DoublyLinkedList(Node(100))


def get_instance():
    linked_list = DoublyLinkedList(Node(100))
    linked_list.append(Node(200))
    linked_list.append(Node(300))
    linked_list.append(Node(400))
    return linked_list


class DoublyLinkedListNode(TestCase):
    def test_has_None_as_next_default(self):
        self.assertIs(Node(1).next, None)

    def test_has_next(self):
        node = Node(1)
        second_node = Node(2)
        node.next = second_node
        self.assertIs(node.next, second_node)

    def test_has_previous(self):
        node = Node(1)
        second_node = Node(2)
        node.previous = second_node
        self.assertIs(node.previous, second_node)


class DoublyLinkedTestCase(TestCase):
    def test_initialization(self):
        linked = get_simple_instance()

        self.assertIsInstance(linked, DoublyLinkedList)

    def test_append(self):
        linked = get_simple_instance()
        linked.append(Node(200))

        self.assertEqual(linked.as_list(), [100, 200])

    def test_append_adds_next(self):
        linked = get_simple_instance()
        second_node = Node(200)
        linked.append(second_node)

        self.assertIs(linked.first_node.next, second_node)

    def test_append_adds_previous(self):
        linked = get_simple_instance()
        second_node = Node(200)
        linked.append(second_node)

        self.assertIs(second_node.previous, linked.first_node)

    def test_insert(self):
        linked = get_instance()
        second_node = Node(1000)
        linked.insert(second_node, 2)

        self.assertEqual(linked.as_list(),
                         [100, 200, 1000, 300, 400])

    def test_insert_at_the_beginning(self):
        linked = get_instance()
        second_node = Node(1000)
        linked.insert(second_node, 0)

        self.assertEqual(linked.as_list(),
                         [1000, 100, 200, 300, 400])

    def test_insert_at_position_one(self):
        linked = get_instance()
        second_node = Node(1000)
        linked.insert(second_node, 1)

        self.assertEqual(linked.as_list(),
                         [100, 1000, 200, 300, 400])

    def test_insert_at_the_end(self):
        linked = get_instance()
        second_node = Node(1000)
        linked.insert(second_node, 3)

        self.assertEqual(linked.as_list(),
                         [100, 200, 300, 1000, 400])

    def test_raises_if_index_is_too_high(self):
        linked = get_instance()
        second_node = Node(1000)

        with self.assertRaises(ValueError):
            linked.insert(second_node, 4)

    def test_raises_if_index_is_too_high_with_simple_instance(self):
        linked = get_simple_instance()
        second_node = Node(1000)

        with self.assertRaises(ValueError):
            linked.insert(second_node, 1)

    def test_raises_if_index_is_too_high_with_empty_instance(self):
        linked = DoublyLinkedList()
        second_node = Node(1000)

        with self.assertRaises(ValueError):
            linked.insert(second_node, 1)

    def test_remove(self):
        linked = get_instance()
        linked.remove(2)

        self.assertEqual(linked.as_list(), [100, 200, 400])

    def test_remove_at_beginning(self):
        linked = get_instance()
        linked.remove(0)

        self.assertEqual(linked.as_list(), [200, 300, 400])

    def test_remove_at_end(self):
        linked = get_instance()
        linked.remove(3)

        self.assertEqual(linked.as_list(), [100, 200, 300])

    def test_remove_from_single_element_list(self):
        linked = get_simple_instance()
        linked.remove(0)

        self.assertEqual(linked.as_list(), [])

    def test_remove_raises_if_index_is_too_high(self):
        linked = get_instance()

        with self.assertRaises(ValueError):
            linked.remove(10)

    def test_remove_raises_if_index_is_lower_than_zero(self):
        linked = get_instance()

        with self.assertRaises(ValueError):
            linked.remove(-3)

    def test_remove_from_empty_list_raises(self):
        linked = DoublyLinkedList()

        with self.assertRaises(ValueError):
            linked.remove(0)

    def test_prepend_adds_an_element_at_the_beginning(self):
        first_node = Node(100)
        node = Node(1000)
        linked = DoublyLinkedList(first_node)
        linked.prepend(node)

        self.assertEqual(linked.as_list(), [1000, 100])
        self.assertIs(linked.first_node, node)
        self.assertIs(linked.first_node.next, first_node)
        self.assertIs(first_node.previous, node)

    def test_prepend_adds_an_element_at_the_beginning_even_without_a_first_node(self):
        linked = DoublyLinkedList()
        node = Node(1000)
        linked.prepend(node)

        self.assertEqual(linked.as_list(), [1000])
        self.assertIs(linked.first_node, node)
        self.assertIs(linked.first_node.next, None)
        self.assertIs(linked.first_node.previous, None)
