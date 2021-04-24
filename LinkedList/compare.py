#!/bin/python3


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def compare_lists(llist1, llist2):
    while llist1 and llist2 and llist1.data == llist2.data:
        llist1 = llist1.next
        llist2 = llist2.next
    return 1 if llist1 == llist2 else 0


if __name__ == '__main__':
    llist1 = SinglyLinkedList()
    test_data = [1, 2, 3]

    for i in range(3):
        llist1_item = test_data[i]
        llist1.insert_node(llist1_item)

    llist2 = SinglyLinkedList()
    for i in range(3):
        llist2_item = test_data[i]
        llist2.insert_node(llist2_item)

    result = compare_lists(llist1.head, llist2.head)
    print(result)
