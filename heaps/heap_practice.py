class MinHeap:
    def __init__(self):
        self.heap = []


    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)


    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def _bubble_up(self, i):
        parent = (i - 1) // 2

        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _bubble_down(self, i):
        n = len(self.heap)

        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

h = MinHeap()
h.push(5)
h.push(2)
h.push(8)
h.push(1)

print(h.pop())
print(h.pop())
print(h.pop())