# def Sorted_Merge(big_arr, small_arr):
#   j = 0
#   while small_arr:
#     added = False
#     for i in range(len(big_arr)):
#       if small_arr[j] < big_arr[i]:
#         big_arr.insert(i, small_arr.pop(j))
#         added = True
#         break
#     if not added:
#       big_arr.append(small_arr.pop(j))
#   return big_arr

# def Sorted_Merge_2(big_arr, small_arr):
#   N = len(big_arr) + len(small_arr)
#   result = [None] * N
#   i = 0
#   while (not all(result)) and big_arr and small_arr:
#     if big_arr[0] < small_arr[0]:
#       result[i] = big_arr.pop(0)
#       i += 1
#     else:
#       result[i] = small_arr.pop(0)
#       i += 1
#   while small_arr:
#     result[i] = small_arr.pop(0)
#     i += 1
#   while big_arr:
#     result[i] = big_arr.pop(0)
#     i += 1
#   return result

# big = [0, 4, 7, 9, 11, 12, 20]
# small = [1, 5, 5, 8, 12]

# Sorted_Merge(big, small)

# Sorted_Merge_2(big, small)

def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return
    k = m
    while nums2:
        swapped = False
        for i in range(m):
            if nums2[0] <= nums1[i]:
                nums1[i], nums1[k] = nums1[k], nums1[i]
                nums1[i] = nums2.pop(0)
                swapped = True
                k += 1
                temp = i+1
                break
        if not swapped:
            nums1[k] = nums2.pop(0)
            m += 1
            k += 1
            continue
        for i in range(temp,k):
            if i == k-1:
                break
            nums1[i], nums1[k-1] = nums1[k-1], nums1[i]
        m += 1

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
merge(nums1, m, nums2, n)

nums1