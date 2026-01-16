from collections import deque

q = deque()
print(q)


# Enqueue - add element to the right side O(1)
q.append(5)
q.append(6)
q.append(7)
print(q)

# Dequeue - remove element from the left side - O(1)
q.popleft()
print(q)


# Peek - get the first element without removing it - O(1)
print(q[0])