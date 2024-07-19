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
        while temp:
            print(temp.data, "->", end='')
            temp = temp.next
        print("None")

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
            return False
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False


# Creating a LinkedList with a cycle for testing
ll = LinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(0)
ll.insert(-4)

# Creating a cycle manually
ll.head.next.next.next.next = ll.head.next  # pos = 1 means -4 points back to 2

# Checking for a cycle
result = ll.ElementMeet()
print("Cycle Detected:", result)
