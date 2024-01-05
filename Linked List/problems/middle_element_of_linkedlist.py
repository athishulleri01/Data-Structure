# Middle of the Linked List
# Problem Statement :-
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]

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

    def middleElement(self):
        if self.head is None:
            return self.head
        
        slow = self.head
        fast = self.head.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(6)

middle = ll.middleElement()
print(middle.data)