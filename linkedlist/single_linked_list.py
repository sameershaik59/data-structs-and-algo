class SinglyNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    head = SinglyNode(1)
    A = SinglyNode(2, head)
    B = SinglyNode(3, A)
    C = SinglyNode(4, B)

    # head.next = A
    # A.next = B
    # B.next = C

    # print(head)


    # traversal - O(n)

    # curr = C

    # while curr:
    #     print(curr.data)
    #     curr = curr.next

    # display linked list - O(n)

    def display(head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(' -> '.join(elements)) #join ['a', 'b', 'c'] 'a -> b -> c'

    # search for node value = O(n)
    def search(head, val):
        curr = head
        while curr:
            if val == curr.data:
                return True
            curr = curr.next

        return False


    display(C)
    print(search(C, 2))