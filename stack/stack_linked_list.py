class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class StackLinkedList:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        self._top = Node(item, self._top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        val = self._top.value
        self._top = self._top.next
        self._size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.value

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._size

    def clear(self):
        self._top = None
        self._size = 0

    def __str__(self):
        values = []
        cur = self._top
        while cur is not None:
            values.append(cur.value)
            cur = cur.next
        return f"Stack(top -> bottom): {values}"


if __name__ == "__main__":
    s = StackLinkedList()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s)
    print(s.peek())
    print(s.pop())
    print(s.size())
    print(s)