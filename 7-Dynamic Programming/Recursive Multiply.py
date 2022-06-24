def recursive_multiply(max, min):
  if min == 0:
    return 0
  return max + recursive_multiply(max, min-1)

recursive_multiply(5, 3)

recursive_multiply(16, 3)