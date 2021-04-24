#!/bin/python3


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def print_singly_linked_list(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next
    return result


def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    node.next = llist
    return node


if __name__ == '__main__':
    llist = SinglyLinkedList()
    test_data = [383, 484, 392, 975, 321]

    for i in range(5):
        llist_item = test_data[i]
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print(print_singly_linked_list(llist.head))
    assert print_singly_linked_list(llist.head) == [321, 975, 392, 484, 383]
