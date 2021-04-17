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


def result_singly_linked_list(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next
    return result


def insertNodeAtPosition(head, data, position):
    if not head.data:
        return None

    curr = head
    index = 0
    new_node = SinglyLinkedListNode(data)

    while curr.next:
        if index + 1 == position:
            tail = curr.next
            curr.next = new_node
            new_node.next = tail
            return head
        curr = curr.next
        index += 1
    return head


if __name__ == '__main__':
    llist = SinglyLinkedList()
    test_nodes = [16, 13, 7]

    for i in range(3):
        llist_item = test_nodes[i]
        llist.insert_node(llist_item)

    data = 1
    position = 2
    llist_head = insertNodeAtPosition(llist.head, data, position)
    print(result_singly_linked_list(llist_head))
    assert result_singly_linked_list(llist_head) == [16, 13, 1, 7]
