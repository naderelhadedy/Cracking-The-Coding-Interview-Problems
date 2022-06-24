def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    for next in graph[start]:
      if next not in visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['1', '2', '3'])}

dfs(graph, '0')

class Node:
  def __init__(self, data):
    self.data = data
    self.visited = False
    self.adjacent = []

  def __repr__(self):
    return f"Node({str(self.data)})"

def search(root):
  if root is None:
    return
  print(root, end=', ')
  root.visited = True
  for n in root.adjacent:
    if n.visited == False:
      search(n)

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
zero.adjacent = [one, two]
one.adjacent = [zero, three]
two.adjacent = [zero, four]

search(zero)