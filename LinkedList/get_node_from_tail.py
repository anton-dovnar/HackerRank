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


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def getNode(head, positionFromTail):
    prev = None
    while head:
        next_temp = head.next
        head.next = prev
        prev = head
        head = next_temp

    idx = 0
    while prev:
        if idx == positionFromTail:
            return prev.data
        prev = prev.next
        idx += 1

    return None


if __name__ == '__main__':
    llist = SinglyLinkedList()
    test_data = [1, 2, 3, 4, 5]

    for i in range(5):
        llist_item = test_data[i]
        llist.insert_node(llist_item)

    position = 2
    result = getNode(llist.head, position)
    print(result)
