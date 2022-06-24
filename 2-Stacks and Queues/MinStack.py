class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack_min) == 0 or val <= self.stack_min[-1]:
            self.stack_min.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        if self.stack[-1] == self.stack_min[-1]:
            self.stack_min.pop()
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack_min[-1]

    def display(self):
        return self.stack

stack = MinStack()

stack.display()

stack.push(5)
stack.push(4)
stack.push(1)
stack.push(3)
stack.push(2)

stack.display()

stack.stack_min

stack.getMin()

stack.pop()

stack.display()

stack.getMin()

stack.pop()
stack.pop()
stack.getMin()