"""
bubble sort:
sorting in ascending order by checking 2 elements

time complexity: O(n^2)
space complexity: O(1)

we use bubble sort bc it is easy to understand, but time complexity is not the best


go thru list
take the first element and compare with next element
check if the first is greater then the next
if so swap them

this will repeat until the list is sorted

need 2 loops
first list to go they the list
second list to compare

you use this when the list is almost sorted, for short lists

Repeatedly swap adjacent out-of-order elements.

"""


def bubble_sort(arr):
    for i in range(len(arr) -1 ): #5
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr



arr = [5, 2, 4, 10, 6, 1, 3, 43, 11, 23, 52]
# 1 2 3 4 5 6
print(bubble_sort(arr))