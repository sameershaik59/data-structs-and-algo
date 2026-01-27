def hourglassSum(arr):
    final = []
    for row in range(len(arr)-2):
        for i in range(len(arr[row]) - 2):
            first = sum(arr[row][i:i+3])
            second = arr[row+1][i+1]
            third = sum(arr[row+2][i:i+3])

            final.append(first + second + third)

    return max(final)



arr = [
  [-9, -9, -9, 1, 1, 1],
  [0, -9, 0, 4, 3, 2],
  [-9, -9, -9, 1, 2, 3],
  [0, 0, 8, 6, 6, 0],
  [0, 0, 0, -2, 0, 0],
  [0, 0, 1, 2, 4, 0]
]

print(hourglassSum(arr))