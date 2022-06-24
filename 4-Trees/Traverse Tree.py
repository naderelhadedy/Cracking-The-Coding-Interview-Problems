class Node:
  def __init__(self, val: str):
    self.val = val
    self.left = None
    self.right = None

def in_order(node: Node):
  if node:
    in_order(node.left)
    visit_node(node.val)
    in_order(node.right)
  else:
    return

def visit_node(val: str):
  print(val, end=' ')


D = Node('D')
D.left = Node('C')
D.right = Node('E')
I = Node('I')
I.left = Node('H')
B = Node('B')
B.left = Node('A')
B.right = D
G = Node('G')
G.right = I
root = Node('F')
root.left = B
root.right = G

in_order(root)