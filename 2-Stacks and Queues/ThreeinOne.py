class ThreeStack:

  def __init__(self, cap=2, N=3):
    self.size = cap
    cap *= N
    self.items = [None] * cap
    self.start = [0, cap//3, 2*(cap//3)]
    self.end = [cap//3, 2*(cap//3), cap]

  def push(self, stack, val):
    if stack > 2:
      raise ValueError(f"Stack {stack} does not exist!")
    
    if self.start[stack] >= self.end[stack]:
      raise ValueError(f"Stack {stack} is full!")
    
    self.items[self.start[stack]] = val
    self.start[stack] += 1

  def pop(self, stack):
    if stack > 2:
      raise ValueError(f"Stack {stack} does not exist!")
    
    top = self.start[stack] - 1
    if top < 0 or self.items[top] == None:
      raise ValueError(f"Stack {stack} is empty! Can't pop!")
    if top < self.end[stack]-self.size:
      raise ValueError(f"Stack {stack} is empty! Can't pop!")

    item = self.items[top]
    self.items[top] = None
    self.start[stack] = top
    return item

  def peek(self, stack):
    if stack > 2:
      raise ValueError(f"Stack {stack} does not exist!")

    top = self.start[stack] - 1
    if top < 0 or self.items[top] == None:
      raise ValueError(f"Stack {stack} is empty! Can't peek!")
    if top < self.end[stack]-self.size:
      raise ValueError(f"Stack {stack} is empty! Can't peek!")

    return self.items[top]

  def display(self):
    print(self.items)

stack = ThreeStack()

stack.push(0,1)

stack.push(0,2)

# stack.push(0,3)

stack.push(1,3)
stack.push(1,4)

stack.push(2,5)
stack.push(2,6)

stack.display()

stack.peek(1)

stack.pop(1)

stack.peek(1)

stack.pop(1)

# stack.pop(1)

stack.display()