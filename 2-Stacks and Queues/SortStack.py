class Stack:
  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if self.isEmpty():
      return
    return self.stack.pop()
  
  def peek(self):
    if self.isEmpty():
      return
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def display(self):
    return self.stack

  def sort(self):
    temp_stack = Stack()
    while not self.isEmpty():
      temp = self.pop()
      while(not temp_stack.isEmpty() and temp_stack.peek() > temp):
          self.push(temp_stack.pop())
      temp_stack.push(temp)

    while not temp_stack.isEmpty():
      self.push(temp_stack.pop())

stack = Stack()

stack.push(4)
stack.push(7)
stack.push(9)
stack.push(1)

stack.display()

stack.sort()

stack.display()