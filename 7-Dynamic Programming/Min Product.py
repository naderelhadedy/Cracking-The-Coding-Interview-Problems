def minProduct(a: int, b: int):
  bigger = b if a < b else a
  smaller = a if a < b else b
  return minProductHelper(smaller, bigger)

def minProductHelper(smaller: int, bigger: int):
  if smaller == 0:
    return 0
  elif smaller == 1:
    return bigger

  s = smaller >> 1 # Divide by 2 
  halfProd = minProductHelper(s, bigger)
 
  if smaller % 2 == 0:
    return halfProd + halfProd
  else:
    return halfProd + halfProd + bigger

minProduct(5, 3)

minProduct(5, 4)