def find_in_nosize(array, target):
  i = -1
  while True:
    try:
      array[i+1]
    except:
      break
    if array[i+1] != target:
      i += 1
    else:
      return i+1
  return -1

find_in_nosize([1, 2, 5, 12, 20, 23], 12)

find_in_nosize([1, 2, 5, 12, 20, 23], 22)