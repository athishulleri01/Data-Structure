class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
#  -----------------------------------------------insertion Start------------------------------------------>
# insert new Node to the linked list
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

# insert new Node to the beggning of linked list
    def insertElementFirst(self,data):
        print()
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.prev = None
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
# insert new Node to the End of linked list
    def insertElementLast(self,data):
        print()
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.prev = None
            self.tail = new_node
        else:
            new_node.prev= self.tail
            self.tail.next=new_node
            self.tail = new_node
            
    def insertAtPosition(self, data, pos):
        
            
#  -----------------------------------------------insertion End------------------------------------------>

#  -----------------------------------------------Traversing Start------------------------------------------>
                    
    def displayForword(self):
        print()
        if self.head is None:
            print("list empty")
            return
        temp = self.head
        while temp:
            print(temp.data,"->",end="")
            temp= temp.next
            
    def displayBackword(self):
        print()
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

dl.insertElementFirst(10)
dl.displayForword()

dl.insertElementLast(13)
dl.displayForword()