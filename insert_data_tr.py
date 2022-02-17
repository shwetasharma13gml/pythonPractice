class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None
    def insert(self,data):
        if self.data:
            if data <self.data:
                if self.left is None:
                    self.left =Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right =Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data =data
    def Printtree(self):
        if self.left:
            self.left.Printtree()
        print(self.data),
        if self.right:
            self.right.Printtree()
    def findval(self,lkpval):
        if lkpval <self.data:
            if self.left is None:
                return str(lkpval) +"  Not found"
            return self.left.findval(lkpval)
        elif lkpval>self.data:
                if self.right is None:
                    return str(lkpval) + "  Not found"
                return self.right.findval(lkpval)
        else:
            print(str(self.data)+' is found')




root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.Printtree()



print(root.findval(7))
print(root.findval(14))
