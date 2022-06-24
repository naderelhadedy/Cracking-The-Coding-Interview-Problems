def selection_sort(array):
  for i in range(len(array)-1):
    min = i
    for j in range(i+1, len(array)):
      if array[j] < array[min]:
        min = j
    array[i], array[min] = array[min], array[i]
  return array

arr = [5, 7, 1, 4, 12, 0]
selection_sort(arr)