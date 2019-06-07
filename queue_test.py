from unittest import TestCase
from queue import SinglyLinkedListQueue, ArrayQueue, PriorityQueue


class QueueTest(TestCase):
    QueueClass = SinglyLinkedListQueue

    def test_enqueues_a_value(self):
        queue = self.QueueClass(5)
        queue.enqueue(10)

        self.assertEqual(queue.as_list_of_values(), [10])

    def test_enqueues_multiple_values(self):
        queue = self.QueueClass(5)
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.as_list_of_values(), [10, 20, 30])

    def test_enqueue_raises_when_queue_is_empty(self):
        queue = self.QueueClass(5)
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        queue.enqueue(40)
        queue.enqueue(50)

        with self.assertRaises(ValueError):
            queue.enqueue(1000)

    def test_dequeues_a_value(self):
        queue = self.QueueClass(5)
        queue.enqueue(10)
        value = queue.dequeue()

        self.assertEqual(value, 10)
        self.assertEqual(queue.as_list_of_values(), [])

    def test_dequeues_multiple_values(self):
        queue = self.QueueClass(5)
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        queue.dequeue()
        value = queue.dequeue()

        self.assertEqual(value, 20)
        self.assertEqual(queue.as_list_of_values(), [30])

    def test_dequeue_raises_when_queue_is_empty(self):
        queue = self.QueueClass(5)

        with self.assertRaises(ValueError):
            queue.dequeue()

    def test_length_increase(self):
        queue = self.QueueClass(2)
        queue.enqueue(10)
        queue.enqueue(20)

        with self.assertRaises(ValueError):
            queue.enqueue(30)

        queue.increase_max_length()
        queue.enqueue(30)

        with self.assertRaises(ValueError):
            queue.enqueue(30)

        self.assertEqual(queue.as_list_of_values(), [10, 20, 30])


class ArrayQueueTest(QueueTest):
    QueueClass = ArrayQueue


class PriorityQueueTest(QueueTest):
    QueueClass = PriorityQueue

    def test_enqueue_operation_respects_priority(self):
        queue = self.QueueClass(5)
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(1)

        self.assertEqual(queue.as_list_of_values(), [1, 10, 20])
