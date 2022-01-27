class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class bit_search:
    def __init__(self):
        self.root = None
    def insert_value(self,node,data):
        if node == None:
            node = Node(data)
        else:
            if data <= node.key:
                node.left = self.insert_value(node.left, data)
            else:
                node.right = self.insert_value(node.right, data)
        return node
    def insert__(self,data):
        self.root = self.insert_value(self.root , data)
        return self.root
    def find(self, root,key):
        if root == None or root.key == key:
            return root is not None
        elif key < root.key:
            return self.find(root.left,key)
        else:
            return self.find(root.right,key)

c= [50,4,24,36,45,72,6]
bst = bit_search()
for i in c:
    bst.insert_value(bst.root,i)

print(bst.find(bst.root,6))

