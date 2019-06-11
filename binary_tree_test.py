from unittest import TestCase
from binary_tree import Node, BinaryTree


class BinaryTreeNodeTest(TestCase):
    def test_has_left_attribute(self):
        node = Node(10)

        self.assertIsNone(node.left)

    def test_has_right_attribute(self):
        node = Node(10)

        self.assertIsNone(node.right)

    def test_has_parent_attribute(self):
        node = Node(10)

        self.assertIsNone(node.parent)

    def test_accepts_parent_node(self):
        parent_node = Node(10)
        node = Node(20, parent_node)

        self.assertIs(node.parent, parent_node)

    def test_accepts_value(self):
        node = Node(10)

        self.assertEqual(node.value, 10)


class BinaryTreeTestcase(TestCase):
    def test_has_root_node_attribute(self):
        bt = BinaryTree()

        self.assertIsNone(bt.root)

    def test_inserts_first_node_as_root_node(self):
        bt = BinaryTree()
        bt.insert(10)

        self.assertIs(bt.root.value, 10)

    def test_does_not_insert_subsequent_node_as_root_node(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(20)

        self.assertEqual(bt.root.value, 10)

    def test_inserts_value_to_the_left_if_smaller(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(1)

        self.assertEqual(bt.root.left.value, 1)

    def test_inserts_value_to_the_left_if_smaller_second_level(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(2)
        bt.insert(1)

        self.assertEqual(bt.root.left.left.value, 1)

    def test_inserts_value_to_the_left_and_then_right(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(1)
        bt.insert(5)

        self.assertEqual(bt.root.left.right.value, 5)

    def test_inserts_value_to_the_right_if_greater(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(11)

        self.assertEqual(bt.root.right.value, 11)

    def test_inserts_value_to_the_right_if_greater_second_level(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(11)
        bt.insert(12)

        self.assertEqual(bt.root.right.right.value, 12)

    def test_inserts_value_to_the_right_and_then_left(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(20)
        bt.insert(15)

        self.assertEqual(bt.root.right.left.value, 15)

    def test_throws_when_adding_an_already_existing_value(self):
        bt = BinaryTree()
        bt.insert(10)

        with self.assertRaises(ValueError):
            bt.insert(10)

    def test_throws_when_adding_an_already_existing_value_with_multiple_values_tree(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(11)
        bt.insert(21)
        bt.insert(301)
        bt.insert(1)

        with self.assertRaises(ValueError):
            bt.insert(10)

    def test_structure(self):
        bt = BinaryTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])

        self.assertEqual(bt.root.value, 10)
        self.assertEqual(bt.root.left.value, 3)
        self.assertEqual(bt.root.left.right.value, 7)
        self.assertEqual(bt.root.left.right.left.value, 4)

    def test_search_root_value(self):
        bt = BinaryTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(10)

        self.assertEqual(node.value, 10)
        self.assertEqual(depth, 0)

    def test_search_first_use_case(self):
        bt = BinaryTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(3)

        self.assertEqual(node.value, 3)
        self.assertEqual(depth, 1)

    def test_search_second_use_case(self):
        bt = BinaryTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(7)

        self.assertEqual(node.value, 7)
        self.assertEqual(depth, 2)

    def test_third_second_use_case(self):
        bt = BinaryTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(4)

        self.assertEqual(node.value, 4)
        self.assertEqual(depth, 3)
