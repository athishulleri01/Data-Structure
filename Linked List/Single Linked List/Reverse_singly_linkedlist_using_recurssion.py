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
    def reverseUtil(self,current,prev):
        if current.next is None:
            self.head = current # we set the head to current node , now we point to the last element ,so we can traverse reversly
            current.next = prev
            return
        
        next = current.next
        current.next = prev
        
        self.reverseUtil(next,current)
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head,None)
        

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(4)
ll.insert(5)

ll.display()
ll.reverse()

ll.display()