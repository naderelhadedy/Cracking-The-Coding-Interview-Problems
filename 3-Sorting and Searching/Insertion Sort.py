def insertion_sort(array):
  for i in range(1, len(array)):
    j = i
    while j > 0 and array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
      j -= 1
  return array

arr = [5, 7, 1, 4, 12, 0]
insertion_sort(arr)