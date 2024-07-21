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
            
#  -----------------------------------------------insertion Start------------------------------------------>
# insert new Node to the linked list
    def insert(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.last = n
        else:
            self.last.next = n
            self.last = n

# insert new Node to the beggning of linked list
    def inserAtBegin(self, data):
        x = Node(data)
        if self.head is None:
            self.head = x
            self.last = self.head
        else:
            x.next = self.head
            self.head = x

# insert new Node to the Last position of the linked list
    def insertAtLast(self, data):
        x = Node(data)
        if self.head is None:
            self.head = x
            self.last = self.head
        else:
            self.last.next = x
            self.last = x
   
# insert new Node to the the specified position of the linked list 
    def insertAtPosition(self, data, index):
        if self.head is None:
            print("list empty")
        else:
            temp = self.head
            it = 0
            prev = None
            if iter == 0:
                self.deleteAtBegin()
                return
            while temp:
                if it == index:
                    nw = Node(data)
                    nw.next = prev.next
                    prev.next = nw
                it += 1
                prev = temp
                temp = temp.next
# insert new Node after the specified element
    def insertAfterElement(self,data,element):
        if self.head is None:
            print("Element not found in this linked list")
            return
        data = Node(data=data)
        temp = self.head
        while(temp.data != element):
            temp = temp.next
        data.next = temp.next
        temp.next = data
        
# insert new Node before the specified position of the list
    def insertBeforeElement(self,data,element):
        if self.head is None:
            print("Element not found in this linked list")
            return
        data = Node(data=data)
        temp = self.head
        while(temp.next.data != element):
            temp = temp.next
            
        data.next = temp.next
        temp.next = data
#  -----------------------------------------------Insertion End------------------------------------------>
                                 
#  -----------------------------------------------Deletion Start------------------------------------------>
# delete Node from beggining of linked list
    def deleteAtBegin(self):
        if self.head is None:
            print("list empty")
        else:
            self.head = self.head.next
            print("element deleted successfully")
            
# delete Node from End of linked list
    def deleteAtEnd(self):
        if self.head is None:
            print("list empty")
        else:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None
   
# delete Node from specified position of linked list
    def deleteAtPosition(self, pos):
        if self.head is None:
            print("list empty")
        else:
            temp = self.head
            prev = None
            it = 0
            while temp:
                if it == pos:
                    prev.next = prev.next.next
                    return
                it += 1
                prev = temp
                temp = temp.next
                

#  -----------------------------------------------Deletion End------------------------------------------>
    


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(4)
ll.insert(5)

ll.display()
ll.inserAtBegin(3)
ll.display()
ll.insertAtLast(6)
ll.display()
ll.deleteAtBegin()
ll.display()
ll.insertAfterElement(10, 2)
ll.display()
ll.insertBeforeElement(20, 2)
ll.display()
ll.insertAtPosition(100,2)
ll.display()
ll.deleteAtBegin()
ll.display()
ll.deleteAtEnd()
ll.display()
ll.deleteAtPosition(2)
ll.display()




    
    