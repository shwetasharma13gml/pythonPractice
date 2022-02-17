class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None

    def Printtree(self):
        print(self.data)
root =Node(27)
root.Printtree()
