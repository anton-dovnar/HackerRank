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


def has_cycle(head):
    if not head:
        return False
    walker = head
    runner = head.next
    while walker != runner:
        if not runner or not runner.next:
            return False
        walker = walker.next
        runner = runner.next.next
    return True


if __name__ == '__main__':
    index = 1
    llist = SinglyLinkedList()
    list_count = 4
    test_data = [1, 2, 3, 4]

    for i in range(list_count):
        llist_item = test_data[i]
        llist.insert_node(llist_item)

    extra = SinglyLinkedListNode(-1)
    temp = llist.head

    for i in range(list_count):
        if i == index:
            extra = temp

        if i != list_count-1:
            temp = temp.next

    temp.next = extra
    result = has_cycle(llist.head)
    print(result)
