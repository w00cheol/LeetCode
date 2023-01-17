import sys

class MinStack:
    def __init__(self):
        self.num_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.num_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.num_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.num_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]