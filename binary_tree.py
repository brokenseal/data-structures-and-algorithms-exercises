class BinaryTreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def pre_order(self):
        # root, left, right
        result = [self.value]
        if self.left is not None:
            result.extend(self.left.pre_order())
        if self.right is not None:
            result.extend(self.right.pre_order())
        return result

    def in_order(self):
        # left, root, right
        result = []
        if self.left is not None:
            result.extend(self.left.in_order())
        result.append(self.value)
        if self.right is not None:
            result.extend(self.right.in_order())
        return result

    def post_order(self):
        # left, right, root
        result = []
        if self.left is not None:
            result.extend(self.left.post_order())
        if self.right is not None:
            result.extend(self.right.post_order())
        result.append(self.value)
        return result

class BinarySearchTreeNode(BinaryTreeNode):
    def insert(self, node):
        if node.value == self.value:
            raise ValueError()

        if node.value < self.value:
            if self.left is None:
                self.left = node
                return
            self.left.insert(node)
            return
        if self.right is None:
            self.right = node
            return
        self.right.insert(node)

    def search(self, value, depth):
        depth += 1
        if self.value == value:
            return self, depth

        if value < self.value:
            if self.left is None:
                return None, depth
            return self.left.search(value, depth)

        if self.right is None:
            return None, depth
        return self.right.search(value, depth)


class BinaryTree:
    Node = BinaryTreeNode

    def __init__(self):
        self.root = None

    def breadth_first(self):
        if self.root is None:
            return [], 0
        current_nodes = [self.root]
        result = []
        depth = -1
        while len(current_nodes) != 0:
            depth += 1
            result.extend([node.value for node in current_nodes])
            next_nodes = []
            for node in current_nodes:
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            current_nodes = next_nodes
        return result, depth

    def pre_order(self):
        if self.root is None:
            return []
        return self.root.pre_order()

    def in_order(self):
        if self.root is None:
            return []
        return self.root.in_order()

    def post_order(self):
        if self.root is None:
            return []
        return self.root.post_order()

class BinarySearchTree(BinaryTree):
    Node = BinarySearchTreeNode

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return
        self.root.insert(self.Node(value))

    def insert_multiple_values(self, values):
        for value in values:
            self.insert(value)

    def search(self, value):
        if self.root is None:
            return None, 0
        return self.root.search(value, -1)

    def delete(self, value, root=None):
        if root is None:
            root = self.root

        if root is None:
            return None

        if value < root.value:
            root.left = self.delete(value, root.left)
        elif value > root.value:
            root.right = self.delete(value, root.right)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_value = calculate_min_value(root.right)
                root.value = min_value
                root.right = self.delete(min_value, root.right)
        return root


def calculate_min_value(root):
    min_value = root.value

    while root.left is not None:
        min_value = root.left.value
        root = root.value
    return min_value
