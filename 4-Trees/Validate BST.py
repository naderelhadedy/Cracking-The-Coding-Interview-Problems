def checkBST(root, min, max):
  if root is None:
    return True
  if ((min != None and root.data <= min) or (max != None and root.data >= max)):
    return False
  l = checkBST(root.left, min, root.data)
  r = checkBST(root.right, root.data, max)
  if ((not l) or (not r)):
    return False
  return True

checkBST(bst, None, None)

new = Node(5)
new.left = Node(3)
new.right = Node(10)
new.left.left = Node(1)
new.left.right = Node(6)

checkBST(new, None, None)