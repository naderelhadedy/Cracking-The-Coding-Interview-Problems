def merge_sort(array):
  if len(array) == 1:
    return array
  
  mid = len(array)//2
  start = 0
  end = len(array)

  left_array = array[start:mid]
  right_array = array[mid:end]
  
  return merge(merge_sort(left_array), merge_sort(right_array))

def merge(left, right):
  merged_list = []
  while (left and right):
    if left[0] < right[0]:
      merged_list.append(left.pop(0))
    else:
      merged_list.append(right.pop(0))
  while right:
    merged_list.append(right.pop(0))
  while left:
    merged_list.append(left.pop(0))
  return merged_list

arr = [5, 7, 1, 4, 12, 0]
merge_sort(arr)