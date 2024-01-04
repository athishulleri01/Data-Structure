class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        data = Node(data)
        if self.head is None:
            self.head = data
            self.prev = None
            self.tail = data
        else:
            data.prev = self.tail
            self.tail.next=data
            self.tail = data

    def displayForword(self):
        if self.head is None:
            print("list empty")
            return
        temp = self.head
        while temp:
            print(temp.data,"->",end="")
            temp= temp.next
    def displayBackword(self):
        if self.head is None:
            print("list empty")
            return
        temp = self.tail
        while temp:
            print(temp.data,"->",end="")
            temp= temp.prev


dl = DoublyLinkedList()
dl.insert(1)
dl.insert(2)
dl.insert(3)
dl.insert(4)
dl.insert(5)

dl.displayForword()
dl.displayBackword()