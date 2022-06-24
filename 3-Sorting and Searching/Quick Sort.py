def quick_sort(array, low, high):
  if low < high:
    pivot_ind = partition(array, low, high)
    quick_sort(array, low, pivot_ind-1)
    quick_sort(array, pivot_ind+1, high)
  # return array

def partition(array, low, high):
  pivot = array[high]
  i = low - 1 # position of greater element
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
  
  array[i+1], array[high] = array[high], array[i+1]
  return i+1

arr = [5, 7, 1, 4, 12, 0]
quick_sort(arr, 0, len(arr)-1)
arr