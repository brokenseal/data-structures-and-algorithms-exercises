class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

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
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self.root.insert(Node(value))

    def insert_multiple_values(self, values):
        for value in values:
            self.insert(value)

    def search(self, value):
        if self.root is None:
            return None, 0
        return self.root.search(value, -1)
