#!/bin/python3


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next
    return result


def reverse(head):
    prev = head.prev
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


if __name__ == '__main__':
    test_data = [1, 2, 3, 4]
    llist = DoublyLinkedList()
    for i in range(4):
        llist_item = test_data[i]
        llist.insert_node(llist_item)

    llist1 = reverse(llist.head)
    print(print_doubly_linked_list(llist1))
    assert print_doubly_linked_list(llist1) == list(reversed(test_data))
