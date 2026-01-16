class Node:
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, name):
        new = Node(name)
        if self.head is None: #empty list
            self.head = new
            self.tail = new
        self.tail.next = new
        self.tail = new

    def display(self):
        curr = self.head
        while curr:
            print(curr.name, end='-> ')
            curr = curr.next
        print('None')

    def search(self, name):
        curr = self.head
        while curr:
            if name == curr.name:
                return True
            curr = curr.next
        return False

    def remove(self, name):
        curr = self.head
        if curr is None:
            return
        if curr.name == name:
            self.head = curr.next
            if self.head is None:
                self.tail = None
            return

        while curr.next:
            if curr.next.name == name:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                return
            curr = curr.next


ll = LinkedList()
ll.append("Ava")
ll.append("Ben")
ll.append("Chris")
ll.append("Dana")

ll.display()
