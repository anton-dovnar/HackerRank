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


def sortedInsert(head, data):
    if not head.data:
        return None

    curr = head
    new_node = DoublyLinkedListNode(data)

    if data < curr.data:
        new_node.next = curr
        curr.prev = new_node
        head = new_node
        return head

    while curr.next:
        if not curr.next.next and curr.next.data <= data:
            curr.next.next = new_node
            new_node.prev = curr.next
            return head
        elif curr.data < data and curr.next.data >= data:
            tail = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next = tail
            tail.prev = new_node
            return head

        curr = curr.next

    return head


if __name__ == '__main__':
    test_data = [1, 3, 4, 10]
    llist_count = 4
    llist = DoublyLinkedList()

    for i in range(llist_count):
        llist_item = test_data[i]
        llist.insert_node(llist_item)

    data = 5
    llist1 = sortedInsert(llist.head, data)
    print(print_doubly_linked_list(llist1))
    assert print_doubly_linked_list(llist1) == [1, 3, 4, 5, 10]
