# Linked List Cycle

# Problem Statement :-
# Input: head = [3,2,0,-4], pos = 1
# Output: true


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

    def ElementMeet(self):
        if self.head is None:
            return self.head
        
        slow = self.head
        fast = self.head.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        
        return False
    

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(6)
result = ll.ElementMeet()
print(result)
