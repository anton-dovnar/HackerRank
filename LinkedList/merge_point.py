def findMergeNode(head1, head2):
    if None in (head1, head2):
        return None

    a = head1
    b = head2

    while a is not b:
        a = head2 if a is None else a.next
        b = head1 if b is None else b.next

    return a.data
