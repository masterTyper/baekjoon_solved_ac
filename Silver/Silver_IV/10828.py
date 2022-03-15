import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return -1 if len(self.items) == 0 else self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return 1 if len(self.items) == 0 else 0

    def top(self):
        return -1 if len(self.items) == 0 else self.items[-1]

N = int(input())

stack = Stack()
for i in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    if command[0] == "top":
        print(stack.top())
    if command[0] == "size":
        print(stack.size())
    if command[0] == "empty":
        print(stack.empty())
    if command[0] == "pop":
        print(stack.pop())
