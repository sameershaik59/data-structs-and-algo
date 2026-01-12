class StackArray:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def clear(self):
        self._data = []

    def __str__(self):
        return f"Stack(bottom -> top): {self._data}"


if __name__ == "__main__":
    s = StackArray()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s)
    print(s.peek())
    print(s.pop())
    print(s.size())
    s.clear()
    print(s)