class LinkedList:
  def __init__(self):
    self.head = None

  def insertAtEnd(self, item):
    new_node = Node(item)
    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

  def print_linkedList(self):
    temp = self.head
    while temp:
      print(str(temp.item), end=' ')
      temp = temp.next

  def remove_dups(self):
    current = self.head
    while current:
      runner = current
      while runner.next:
        if current.item == runner.next.item:
          runner.next = runner.next.next
        else:
          runner = runner.next
      current = current.next

  def kth_to_last(self, k):
    current = runner = self.head
    for i in range(k):
      if runner is None:
        return
      runner = runner.next
    while runner:
      current = current.next
      runner = runner.next
    return current.item

  def remove_middle(self):
    current = runner = self.head
    while runner.next:
      if runner.next.next:
        temp = current
        current = current.next
        runner = runner.next.next
      else:
        break
    temp.next = temp.next.next

class Node:
  def __init__(self, item):
    self.item = item
    self.next = None

lst = [1, 2, 3, 2, 5, 5, 7]

linked_list = LinkedList()
linked_list.head = Node(lst[0])

for i in lst[1:]:
  linked_list.insertAtEnd(i)

linked_list.print_linkedList()

linked_list.remove_dups()

linked_list.print_linkedList()

linked_list.kth_to_last(5)

linked_list.remove_middle()

linked_list.print_linkedList()