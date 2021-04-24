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


def printLinkedList(head):
    if not head:
        return None

    while head:
        print(head.data)
        head = head.next


if __name__ == '__main__':
    llist = SinglyLinkedList()
    test_data = [16, 13]

    for i in range(2):
        llist_item = test_data[i]
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
