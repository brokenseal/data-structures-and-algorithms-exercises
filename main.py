from linked_list import SinglyLinkedList, Node
from doubly_linked_list_test import get_simple_instance

if __name__ == "__main__":
    linked = get_simple_instance()
    linked.append(Node(200))
    print(str(list(linked)))