def binary_search(array, low, high, key):
  '''Array must be sorted'''
  if low == high and array[low] != key:
    return

  mid = (low + high) // 2
  if array[mid] == key:
    return mid

  if key < array[mid]:
    high = mid - 1
    return binary_search(array, low, high, key)
  else:
    low = mid + 1
    return binary_search(array, low, high, key)

arr = [0, 1, 4, 5, 7, 12]
binary_search(arr, 0, len(arr)-1, 7)