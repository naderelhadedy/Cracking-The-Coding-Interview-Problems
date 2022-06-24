class MyQueue:
  def __init__(self):
    self.stack_store = []
    self.stack_return = []

  def enqueue(self, item):
    self.stack_store.append(item)

  def dequeue(self):
    if not self.stack_return:
      self.shift_stack()
    if self.stack_return:
      return self.stack_return.pop()

  def peek(self):
    if not self.stack_return:
      self.shift_stack()
    if self.stack_return:
      return self.stack_return[-1]

  def shift_stack(self):
    while self.stack_store:
      self.stack_return.append(self.stack_store.pop())

queue = MyQueue()

queue.enqueue(3)
queue.enqueue(24)
queue.enqueue(9)

queue.dequeue()

queue.peek()

queue.enqueue(12)
queue.enqueue(30)

queue.peek()

queue.dequeue()

queue.dequeue()

queue.dequeue()

queue.dequeue()

queue.dequeue()

queue.peek()