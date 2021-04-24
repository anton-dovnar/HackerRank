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


def mergeLists(head1, head2):
    dummy = temp = SinglyLinkedListNode(0)
    while head1 and head2:
        if head1.data < head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next

        temp = temp.next
    temp.next = head1 or head2
    return dummy.next


if __name__ == '__main__':
    llist1 = SinglyLinkedList()
    list1_data = [1, 2, 3, 4]

    for i in range(4):
        llist1_item = list1_data[i]
        llist1.insert_node(llist1_item)

    llist2 = SinglyLinkedList()
    list2_data = [-1, 2, 3, 4, 5]

    for i in range(5):
        llist2_item = list2_data[i]
        llist2.insert_node(llist2_item)

    llist3 = mergeLists(llist1.head, llist2.head)

    print(print_singly_linked_list(llist3))
