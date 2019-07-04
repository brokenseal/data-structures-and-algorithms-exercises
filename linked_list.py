class SinglyLinkedList:
    def __init__(self, first_value=None):
        self.first_node = first_value is not None and Node(first_value) or None
        self._reset_for_iteration()

    def append(self, value):
        node = Node(value)
        last_node = None
        for last_node, _, _ in self:
            pass
        if last_node is None:
            self.first_node = node
        else:
            last_node.next = node

    def prepend(self, value):
        node = Node(value)
        previous_first_node = self.first_node
        self.first_node = node
        node.next = previous_first_node

    def insert(self, value, at_index):
        node_to_insert = Node(value)
        if at_index == 0:
            node_to_insert.next = self.first_node
            self.first_node = node_to_insert
            return

        for node, previous_node, index in self:
            if index != at_index:
                continue
            previous_node.next = node_to_insert
            node_to_insert.next = node
            break
        else:
            raise ValueError("Index value too high")

    def remove(self, at_index):
        for node, previous_node, index in self:
            if index != at_index:
                continue
            # if node is None:
            #     raise ValueError("Index too small")
            if previous_node is None:
                removed = self.first_node
                self.first_node = self.first_node.next
                return removed
            previous_node.next = node.next
            return node
        else:
            raise ValueError("Index too big")

    def __str__(self):
        return str([str(node) for node, _, _ in list(self)])

    def _reset_for_iteration(self):
        self._current_node = None
        self._previous_node = None
        self._index = -1

    def __iter__(self):
        self._reset_for_iteration()
        return self

    def __next__(self):
        self._previous_node = self._current_node
        if self._current_node is None:
            self._current_node = self.first_node
        else:
            self._current_node = self._current_node.next

        if self._current_node is None:
            raise StopIteration()

        self._index += 1
        return (self._current_node, self._previous_node, self._index)

    def __getitem__(self, at_index):
        for node, _, index in self:
            if index == at_index:
                return node.value
        raise IndexError("linked list index out of range")

    def __setitem__(self, at_index, value):
        if self.first_node is None and at_index == 0:
            self.first_node = Node(value)
            return

        length = 0
        for node, previous_node, index in self:
            length += 1
            if index != at_index:
                continue

            node_to_add = Node(value)
            if previous_node is None:
                self.first_node = node_to_add
            if previous_node is not None:
                previous_node.set_next(node_to_add)
            node_to_add.set_next(node.next)
            return
        if length == at_index:
            self.append(value)
            return
        raise IndexError("linked list assignment index out of range")

    def as_list(self):
        return [node.value for node, _, _ in self]

    def __eq__(self, cmp):
        return isinstance(cmp, self.__class__) and self.as_list() == cmp.as_list()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next_node=None):
        self.next = next_node

    def __str__(self):
        return str(self.value)

    def __eq__(self, cmp):
        return isinstance(cmp, self.__class__) and self.value == cmp.value and self.next == cmp.next


class StackedSinglyLinkedList(SinglyLinkedList):
    def push(self, node):
        return self.prepend(node)

    def pop(self):
        return self.remove(0)
