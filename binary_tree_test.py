from unittest import TestCase
from binary_tree import BinaryTreeNode, BinarySearchTree, BinaryTree, BinaryTreeNode


class BinaryTreeNodeTest(TestCase):
    def test_has_left_attribute(self):
        node = BinaryTreeNode(10)

        self.assertIsNone(node.left)

    def test_has_right_attribute(self):
        node = BinaryTreeNode(10)

        self.assertIsNone(node.right)

    def test_has_parent_attribute(self):
        node = BinaryTreeNode(10)

        self.assertIsNone(node.parent)

    def test_accepts_parent_node(self):
        parent_node = BinaryTreeNode(10)
        node = BinaryTreeNode(20, parent_node)

        self.assertIs(node.parent, parent_node)

    def test_accepts_value(self):
        node = BinaryTreeNode(10)

        self.assertEqual(node.value, 10)


class BinaryTreeTestCase(TestCase):
    def test_has_root_node_attribute(self):
        bt = BinarySearchTree()

        self.assertIsNone(bt.root)

    def test_inserts_first_node_as_root_node(self):
        bt = BinarySearchTree()
        bt.insert(10)

        self.assertIs(bt.root.value, 10)

    def test_does_not_insert_subsequent_node_as_root_node(self):
        bt = BinarySearchTree()
        bt.insert(10)
        bt.insert(20)

        self.assertEqual(bt.root.value, 10)

    def test_inserts_value_to_the_left_if_smaller(self):
        bt = BinarySearchTree()
        bt.insert(10)
        bt.insert(1)

        self.assertEqual(bt.root.left.value, 1)

    def test_inserts_value_to_the_left_if_smaller_second_level(self):
        bt = BinarySearchTree()
        bt.insert(10)
        bt.insert(2)
        bt.insert(1)

        self.assertEqual(bt.root.left.left.value, 1)

    def test_inserts_value_to_the_left_and_then_right(self):
        bt = BinarySearchTree()
        bt.insert(10)
        bt.insert(1)
        bt.insert(5)

        self.assertEqual(bt.root.left.right.value, 5)

    def test_inserts_value_to_the_right_if_greater(self):
        bt = BinarySearchTree()
        bt.insert(10)
        bt.insert(11)

        self.assertEqual(bt.root.right.value, 11)

    def test_inserts_value_to_the_right_if_greater_second_level(self):
        bt = BinarySearchTree()
        bt.insert(10)
        bt.insert(11)
        bt.insert(12)

        self.assertEqual(bt.root.right.right.value, 12)

    def test_inserts_value_to_the_right_and_then_left(self):
        bt = BinarySearchTree()
        bt.insert(10)
        bt.insert(20)
        bt.insert(15)

        self.assertEqual(bt.root.right.left.value, 15)

    def test_throws_when_adding_an_already_existing_value(self):
        bt = BinarySearchTree()
        bt.insert(10)

        with self.assertRaises(ValueError):
            bt.insert(10)

    def test_throws_when_adding_an_already_existing_value_with_multiple_values_tree(self):
        bt = BinarySearchTree()
        bt.insert(10)
        bt.insert(11)
        bt.insert(21)
        bt.insert(301)
        bt.insert(1)

        with self.assertRaises(ValueError):
            bt.insert(10)

    def test_structure(self):
        bt = BinarySearchTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])

        self.assertEqual(bt.root.value, 10)
        self.assertEqual(bt.root.left.value, 3)
        self.assertEqual(bt.root.left.right.value, 7)
        self.assertEqual(bt.root.left.right.left.value, 4)

    def test_search_root_value(self):
        bt = BinarySearchTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(10)

        self.assertEqual(node.value, 10)
        self.assertEqual(depth, 0)

    def test_search_first_use_case(self):
        bt = BinarySearchTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(3)

        self.assertEqual(node.value, 3)
        self.assertEqual(depth, 1)

    def test_search_second_use_case(self):
        bt = BinarySearchTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(7)

        self.assertEqual(node.value, 7)
        self.assertEqual(depth, 2)

    def test_search_third_use_case(self):
        bt = BinarySearchTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(4)

        self.assertEqual(node.value, 4)
        self.assertEqual(depth, 3)

    def test_deletion_first_use_case(self):
        bt = BinarySearchTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(4)

        self.assertEqual(node.value, 4)
        self.assertEqual(depth, 3)

        bt.delete(4)

        node, depth = bt.search(4)

        self.assertIsNone(node)
        self.assertEqual(bt.in_order(), [
                         3, 7, 10, 20, 22, 32, 900])

    def test_deletion_root(self):
        bt = BinarySearchTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(10)

        self.assertEqual(node.value, 10)
        self.assertEqual(depth, 0)

        bt.delete(10)

        node, _ = bt.search(10)

        self.assertIsNone(node)
        self.assertEqual(bt.in_order(), [
                         3, 4, 7, 20, 22, 32, 900])

    def test_deletion_leaf(self):
        bt = BinarySearchTree()
        bt.insert_multiple_values([10, 20, 22, 3, 7, 4, 32, 900])
        node, depth = bt.search(900)

        self.assertEqual(node.value, 900)
        self.assertEqual(depth, 4)

        bt.delete(900)

        node, _ = bt.search(900)

        self.assertIsNone(node)
        self.assertEqual(bt.in_order(), [
                         3, 4, 7, 10, 20, 22, 32])


class BinaryTreeUtilityMethodsTestCase(TestCase):
    def test_breadth_first(self):
        bt = create_tree_ready_for_traversal()
        result, depth = bt.breadth_first()

        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(depth, 2)

    def test_breadth_first_empty_tree(self):
        bt = BinaryTree()
        result, depth = bt.breadth_first()

        self.assertEqual(result, [])
        self.assertEqual(depth, 0)

    def test_breadth_first_mostly_left_side_nodes(self):
        bt = BinaryTree()
        bt.root = BinaryTreeNode(1)
        bt.root.left = BinaryTreeNode(2)
        bt.root.right = BinaryTreeNode(3)

        bt.root.left.left = BinaryTreeNode(4)
        bt.root.left.right = BinaryTreeNode(5)
        bt.root.right.right = BinaryTreeNode(7)

        bt.root.left.left.left = BinaryTreeNode(6)
        bt.root.left.left.left.left = BinaryTreeNode(8)

        result, depth = bt.breadth_first()

        self.assertEqual(result, [1, 2, 3, 4, 5, 7, 6, 8])
        self.assertEqual(depth, 4)

    def test_pre_order(self):
        bt = create_tree_ready_for_traversal()

        self.assertEqual(bt.pre_order(), [1, 2, 4, 5, 3, 6, 7])

    def test_in_order(self):
        bt = create_tree_ready_for_traversal()

        self.assertEqual(bt.in_order(), [4, 2, 5, 1, 6, 3, 7])

    def test_post_order(self):
        bt = create_tree_ready_for_traversal()

        self.assertEqual(bt.post_order(), [4, 5, 2, 6, 7, 3, 1])


def create_tree_ready_for_traversal():
    #                     ____1____
    #                    |         |
    #                  __2__     __3__
    #                 |     |   |     |
    #                 4     5   6     7
    bt = BinaryTree()
    bt.root = BinaryTreeNode(1)
    bt.root.left = BinaryTreeNode(2)
    bt.root.left.left = BinaryTreeNode(4)
    bt.root.left.right = BinaryTreeNode(5)
    bt.root.right = BinaryTreeNode(3)
    bt.root.right.right = BinaryTreeNode(7)
    bt.root.right.left = BinaryTreeNode(6)
    return bt
