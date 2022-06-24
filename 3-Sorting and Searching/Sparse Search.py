def sparse_search(array, low, high, key):
  '''Array must be sorted'''
  if key == '':
    return
  if (low == high and array[low] != key) or (low == high and array[low] == ''):
    return -1
  if not any(array[low:high+1]):
    return -1

  mid = (low + high) // 2
  while array[mid] == "":
    mid -= 1

  if array[mid] == key:
    return mid
  elif key < array[mid]:
    high = mid - 1
    return sparse_search(array, low, high, key)
  else:
    low = mid + 1
    return sparse_search(array, low, high, key)

arr = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
sparse_search(arr, 0, len(arr)-1, "ball")