class BST:
    def __init__(self,data):
        self.lchild = None
        self.key = data
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            
        if self.key == data:
            return
         
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                
                
    def search(self, data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the lfet tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the right tree")
                
     
                # 
                
                
    # traversal
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.preorder()
        print(self.key)
        if self.rchild:
            self.rchild.preorder()
            
    def postorder(self):
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        print(self.key)

    def maxValue(self):
        if self.rchild:
            self.rchild.maxValue()
        else:
            print(self.key)


    def minValue(self):
        if self.lchild:
            self.lchild.minValue()
        else:
            print(self.key)
            

bst = BST(10)
list1 = [1,2,3,4,5,55,66,7]
for i in list1:
    bst.insert(i)


bst.search(66)
bst.preorder()
print("............")
bst.inorder()
print("............")

bst.postorder()
print("............")
bst.maxValue()
print("............")
bst.minValue()