class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        print()
        while temp:
            print(temp.data, "->", end='')
            temp = temp.next

    def insert(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.last = n
        else:
            self.last.next = n
            self.last = n
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(4)
ll.insert(5)

ll.display()
ll.reverse()

ll.display()