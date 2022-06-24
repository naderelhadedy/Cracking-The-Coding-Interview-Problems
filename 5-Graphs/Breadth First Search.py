import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [1, 2]}
print("Following is Breadth First Traversal: ")
bfs(graph, 0)

class Node:
  def __init__(self, data):
    self.data = data
    self.visited = False
    self.adjacent = []

  def __repr__(self):
    return f"Node({str(self.data)})"

def search(root):
  queue = []
  root.visited = True
  # Add to the end of queue
  queue.append(root) 
  while len(queue) != 0:
    # Remove from the front of the queue
    r = queue.pop(0)
    print(r, end=', ')
    for n in r.adjacent:
      if n.visited == False:
        n.visited = True
        queue.append(n)

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
zero.adjacent = [one, two]
one.adjacent = [zero, three]
two.adjacent = [zero, four]

search(zero)