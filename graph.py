from linked_list import SinglyLinkedList


class Graph:
    def __init__(self, count):
        self.count = count
        self.adj_list_array = SinglyLinkedList()

        for _ in range(0, count):
            self.adj_list_array.append(SinglyLinkedList())

    # def add_edge(self, source, destination):
    #     self.adj_list_array.append()
