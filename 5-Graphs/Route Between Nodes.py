class Node:
  def __init__(self, data):
    self.data = data
    self.adjacent = []
    self.visited = False

  def __repr__(self):
    return f"Node({self.data})"

def have_path(src: Node, dst: Node) -> bool:
  queue = []
  src.visited = True
  queue.append(src)
  while len(queue) != 0:
    node = queue.pop(0)
    for item in node.adjacent:
      if item.visited == False:
        if item.data == dst.data:
          return True
        else:
          item.visited = True
          queue.append(item)
  return False

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
zero.adjacent.extend([two])
one.adjacent.extend([zero])
two.adjacent.extend([three])

have_path(zero, three)

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
zero.adjacent.extend([two])
one.adjacent.extend([zero])
two.adjacent.extend([three])

have_path(zero, two)

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
zero.adjacent.extend([two])
one.adjacent.extend([zero])
two.adjacent.extend([three])

have_path(one, three)

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
zero.adjacent.extend([two])
one.adjacent.extend([zero])
two.adjacent.extend([three])

have_path(zero, one)

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
zero.adjacent.extend([two])
one.adjacent.extend([zero])
two.adjacent.extend([three])

have_path(one, zero)