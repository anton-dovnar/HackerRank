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


def print_singly_linked_list(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next
    return result


def reverse(head):
    prev = None
    while head:
        next_temp = head.next
        head.next = prev
        prev = head
        head = next_temp
    return prev

if __name__ == '__main__':
    llist = SinglyLinkedList()
    test_data = [1, 2, 3]

    for i in range(3):
        llist_item = test_data[i]
        llist.insert_node(llist_item)

    llist1 = reverse(llist.head)
    print(print_singly_linked_list(llist1))
    assert print_singly_linked_list(llist1) == [3, 2, 1]
