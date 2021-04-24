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


def deleteNode(head, position):
    if not head:
        return None

    if position == 0:
        if head.next:
            head = head.next
        else:
            head = None
        return head

    idx = 0
    node = head
    while node.next:
        if idx + 1 == position:
            if node.next.next:
                node.next = node.next.next
            else:
                node.next = None
            break

        node = node.next
        idx += 1
    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()
    test_data = [20, 6, 2, 19, 7, 4, 15, 9]

    for i in range(8):
        llist_item = test_data[i]
        llist.insert_node(llist_item)

    position = 3
    llist1 = deleteNode(llist.head, position)
    print(print_singly_linked_list(llist1))
    assert print_singly_linked_list(llist1) == [20, 6, 2, 7, 4, 15, 9]
