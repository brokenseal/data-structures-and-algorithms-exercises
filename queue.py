from linked_list import SinglyLinkedList, Node


class SinglyLinkedListQueue:
    def __init__(self, max_length):
        self._queue = SinglyLinkedList()
        self._length = 0
        self._max_length = max_length

    def enqueue(self, value):
        if self._length == self._max_length:
            raise ValueError("Overflow")
        self._length += 1
        self._queue.append(value)

    def dequeue(self):
        if self._length == 0:
            raise ValueError("Underflow")
        self._length -= 1
        return self._queue.remove(0).value

    def increase_max_length(self):
        self._max_length += 1

    def as_list_of_values(self):
        return self._queue.as_list_of_values()


class ArrayQueue:
    def __init__(self, max_length):
        self._queue = []
        self._max_length = max_length

    def enqueue(self, value):
        if len(self._queue) == self._max_length:
            raise ValueError("Overflow")
        self._queue.append(value)

    def dequeue(self):
        if len(self._queue) == 0:
            raise ValueError("Underflow")
        removed = self._queue[0]
        self._queue.remove(removed)
        return removed

    def increase_max_length(self):
        self._max_length += 1

    def as_list_of_values(self):
        return [value for value in self._queue]


class PriorityQueue(ArrayQueue):
    def enqueue(self, value):
        super(PriorityQueue, self).enqueue(value)
        self._queue.sort(key=lambda value: value)
