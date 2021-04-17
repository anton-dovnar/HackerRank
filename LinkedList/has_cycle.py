def has_cycle(head):
    try:
        walker = head
        runner = head.next
        while walker is not runner:
            walker = walker.next
            runner = runner.next.next
        return True
    except:
        return False
