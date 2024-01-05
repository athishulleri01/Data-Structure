class Node:
     def __init__(self, data):
          self.data = data
          self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    def display(self):
        print()
        if self.top is None:
            print("stack  underflow")
        else:
            temp = self.top
            while temp:
                print(temp.data,"->",end="")
                temp = temp.next
                
    def pop(self):
        if self.top is None:
            print("stack underflow")
        else:
            self.top = self.top.next
            
            
                
                
st = Stack()
st.push(1)
st.push(2)    
st.push(3)    
st.push(4) 
st.display()
st.pop()
st.display()
   
        
     