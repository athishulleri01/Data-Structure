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
            
    def Dequeue(self):
        if self.isEmpty():
            print("queue overflow")
            return
        self.front = self.front.next
        
                
    def display(self):
        print()
        if self.isEmpty():
            print("queue is underflow")
            return 
        temp = self.front
        while temp:
            print(temp.data,"->",end="")
            temp = temp.next
            
            
            
qu = Queue()
qu.Enqueue(1)
qu.Enqueue(2)
qu.Enqueue(3)
qu.Enqueue(4)
qu.Enqueue(5)

qu.display()

qu.Dequeue()
qu.display()