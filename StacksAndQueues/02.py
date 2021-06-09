"""
A Tale of Two Stacks
"""


class MyQueue(object):
    def __init__(self):
        self.fifo = []
        self.lifo = []

    def peek(self):
        return self.fifo[0]

    def pop(self):
        self.fifo.pop(0)
        self.lifo.pop()

    def put(self, value):
        self.fifo.append(value)
        self.lifo.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
