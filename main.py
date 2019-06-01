from linked_list import SinglyLinkedList, Node

if __name__ == "__main__":
    meh = SinglyLinkedList(Node(100))
    meh.append(Node(200))
    meh.append(Node(300))
    meh.insert(Node(1000), 2)
    meh.insert(Node(2000), 3)
    print(meh)
