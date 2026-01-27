from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)  # O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()  # O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[0]  # O(1)

    def is_empty(self):
        return len(self._data) == 0  # O(1)

    def size(self):
        return len(self._data)  # O(1)

    def __str__(self):
        return f"Queue(front -> back): {list(self._data)}"


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(15)

    print(q)
    print(q.dequeue())   # 5
    print(q.peek())      # 10
    print(q.size())      # 2
    print(q)