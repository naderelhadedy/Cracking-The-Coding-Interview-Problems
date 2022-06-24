def bubble_sort(array):
  for i in range(len(array)):
    swapped = False
    for j in range(0, len(array)-1-i):
      if array[j+1] < array[j]:
        array[j+1], array[j] = array[j], array[j+1]
        swapped = True
    if not swapped:
      break
  return array

arr = [5, 7, 1, 4, 12, 0]
bubble_sort(arr)