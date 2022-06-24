def get_height(root):
  if root is None:
    return -1
  return 1 + max(get_height(root.right), get_height(root.left))

def check_balanced(root):
  if root is None:
    return True
  if abs(get_height(root.left) - get_height(root.right)) <= 1:
    return check_balanced(root.left) and check_balanced(root.right)
  else:
    return False

check_balanced(bst)