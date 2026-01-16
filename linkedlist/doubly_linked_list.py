class DoublyNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)



head = tail = DoublyNode(1)
print(head)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
    print(' <-> '.join(elements))

display(head)


# insert at beginning - O(1)

def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 2)
head, tail = insert_at_beginning(head, tail, 4)
display(head)