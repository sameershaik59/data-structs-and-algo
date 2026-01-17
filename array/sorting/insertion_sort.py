"""
time complexity O(n^2)
space complexity O(1)

go thru list
seperated in sorted and unsorted

take the first element and compare with next element
if next element is smaller then swap them, keep doing this until sorted

Insert each element into its correct spot in the sorted prefix.
"""

def insertion_sort(arr):

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp

            else:
                break

    return arr



arr = [5, 2, 4, 10, 6, 1, 3, 43, 11, 23, 52]
print(insertion_sort(arr))