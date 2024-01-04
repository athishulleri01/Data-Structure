# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         temp = self.head
#         print()
#         while temp:
#             print(temp.data, "->", end='')
#             temp = temp.next

#     def insert(self, data):
#         n = Node(data)
#         if self.head is None:
#             self.head = n
#             self.last = n
#         else:
#             self.last.next = n
#             self.last = n

#     def inserAtBegin(self, data):
#         x = Node(data)
#         if self.head is None:
#             self.head = x
#             self.last = self.head
#         else:
#             x.next = self.head
#             self.head = x

#     def insertAtLast(self, data):
#         x = Node(data)
#         if self.head is None:
#             self.head = x
#             self.last = self.head
#         else:
#             self.last.next = x
#             self.last = x

#     def deleteAtBegin(self):
#         if self.head is None:
#             print("list empty")
#         else:
#             self.head.next = self.head.next.next
#             print("element deleted successfully")



# ll = LinkedList()
# ll.insert(1)
# ll.insert(2)
# ll.insert(4)
# ll.insert(5)

# ll.display()
# ll.inserAtBegin(3)
# ll.display()
# ll.insertAtLast(6)
# ll.display()
# ll.deleteAtBegin()
# ll.display()



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self,data):
        data = Node(data)
        if self.head is None:
            self.head = data
            self.last = self.head
        else:
            self.last.next = data
            self.last = data

    def display(self):
        print()
        temp = self.head
        while temp:
            print(temp.data,"->",end="")
            temp = temp.next
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



ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.display()
ll.insertAfterElement(9,2)
ll.display()
ll.insertBeforeElement(7,5)
ll.display()

    
    