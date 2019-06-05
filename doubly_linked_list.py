class DoublyLinkedList:
    def __init__(self, first_node=None):
        self.first_node = first_node
        self._index = 0
        self._current = None

    def append(self, node_to_append):
        if self.first_node is None:
            self.first_node = node_to_append
            return
        for node, _ in self:
            pass
        node.set_next(node_to_append)

    def insert(self, node_to_insert, at_index):
        if at_index == 0 and self.first_node is None:
            self.first_node = node_to_insert
            return
        for node, index in self:
            if index != at_index:
                continue
            if node.previous is None:
                self.first_node = node_to_insert
                self.first_node.set_next(node)
                break
            node.previous.set_next(node_to_insert)
            node_to_insert.set_next(node)
            break
        else:
            raise ValueError()

    def remove(self, at_index):
        for node, index in self:
            if index != at_index:
                continue
            if node.previous is None:
                self.first_node = self.first_node.next
                break
            node.previous.next = node.next
            if node.next is not None:
                node.next.previous = node.previous
            break
        else:
            raise ValueError()

    def as_list_of_values(self):
        return [node.value for node, _ in self]

    def __iter__(self):
        self._index = -1
        self._current = None
        return self

    def __next__(self):
        self._index += 1
        if self._current is None:
            self._current = self.first_node
        else:
            self._current = self._current.next
        if self._current is None:
            raise StopIteration()
        return self._current, self._index


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def set_next(self, node):
        self.next = node
        node.previous = self
