def binary_search(arr, target): #log(n)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

"""
binary search is always sorted array
time complexity: O(log(n))

logn bc everytime u check the middle element it removes the half

"""


def linear_search(arr, target): #O(n)
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

"""
linear search is not sorted array
time complexity: O(n) because it goes to every element
"""

nums = [1, 3, 5, 7, 9, 12, 15]

print(binary_search(sorted(nums), 9))   # 4
print(binary_search(sorted(nums), 2))   # -1
