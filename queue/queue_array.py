class QueueArray:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.data.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

if __name__ == "__main__":
    q = QueueArray()
    q.enqueue(5)
    q.enqueue(10)
    print(q.dequeue())
    print(q.peek())
    print(q.size())