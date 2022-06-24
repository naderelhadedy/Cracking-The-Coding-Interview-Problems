class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def in_order(root):
  if root:
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)

def make_bst(arr, low, high):
  mid = (low + high) // 2
  if low > high:
    return
  root = Node(arr[mid])
  root.left = make_bst(arr, low, mid-1)
  root.right = make_bst(arr, mid+1, high)
  return root

arr = [1, 3, 4, 6, 8, 10]
bst = make_bst(arr, 0, len(arr)-1)

in_order(bst)