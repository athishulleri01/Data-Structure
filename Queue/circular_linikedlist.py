class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = self.rear = None
        
    def isEmpty(self):
        return self.rear is None
    
    def Enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.rear = self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.rear.next = self.front
            
    def Dequeue(self):
        if self.isEmpty():
            print("queue overflow")
            return
        if (self.front == self.rear):
            # value = self.front.data
            self.front = None
            self.rear = None
        else:
            self.rear.next=self.front.next
            self.front = self.front.next
        
                
    def display(self):
        print()
        if self.isEmpty():
            print("queue is underflow")
            return 
        temp = self.front
        while True:
            print(temp.data,"->",end="")
            temp = temp.next
            if temp == self.front:
                return
            
            
            
qu = Queue()
qu.Enqueue(1)
qu.Enqueue(2)
qu.Enqueue(3)
qu.Enqueue(4)
qu.Enqueue(5)

qu.display()

qu.Dequeue()
qu.display()