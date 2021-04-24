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


def removeDuplicates(head):
    if not head:
        return None

    curr = head
    next_node = head.next
    while next_node:
        if next_node.data == curr.data:
            next_node = next_node.next
            if not next_node:
                curr.next = None
        else:
            curr.next = next_node
            curr = next_node
            next_node = next_node.next

    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()
    test_data = [1, 2, 2, 3, 4, 5, 5]

    for i in range(7):
        llist_item = test_data[i]
        llist.insert_node(llist_item)

    llist1 = removeDuplicates(llist.head)
    print(print_singly_linked_list(llist1))
