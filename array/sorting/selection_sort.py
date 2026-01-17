"""
start to end, find the min value
compare min value to next val
if next val is smaller then update min val
swap first with min


time complexity: O(n^2), lopping through the array twice
space complexity: O(1),

use slection sort because it uses the fewests swaps

swaps are expensive bc it takes time to swap
Repeatedly select minimum and adds to sorted array
"""

# def selection_sort(arr):
#     sorted_arr = []
#     for i in range(len(arr)):
#         sorted_arr.append(min(arr))
#         arr.remove(min(arr))
#
#     return sorted_arr


def selection_sort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                temp = arr[minIndex]
                arr



    return arr

arr = [5, 2, 4, 10, 6, 1, 3, 43, 11, 23, 52]

print(selection_sort(arr))