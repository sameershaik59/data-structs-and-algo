class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class QueueLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        val = self._head.value
        self._head = self._head.next
        self._size -= 1

        if self._head is None:
            self._tail = None

        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def size(self):
        return self._size

    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        values = []
        cur = self._head
        while cur is not None:
            values.append(cur.value)
            cur = cur.next
        return f"Queue(front -> back): {values}"


if __name__ == "__main__":
    q = QueueLinkedList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(q.peek())
    print(q.dequeue())
    print(q.size())
    print(q)