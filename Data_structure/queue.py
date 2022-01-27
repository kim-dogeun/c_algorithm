class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
    
class circlularlinked:
    def __init__(self):   
        self.head = head
        head.next = head
        
    
    def get_nodes(self):
        i = self.head
        while(i.value < i.next.value):
            print(i.key)
            i = i.next
        print(i.key)

    def insert_node(self,node1, node2):
        node2.next = node1.next
        node1.next = node2

    def delete_next(self,node):
        node.next = node.next.next

class queue(circlularlinked):
    def __init__(self):
        circlularlinked.__init__(self)
    
    def put(self,newnode):
        i=self.head
        while(i.value < i.next.value):
            i = i.next
        self.insert_node(i,newnode)

    def get(self):
        print(head.next.key)
        self.delete_next(head)
        i=self.head
        while(i.value < i.next.value):
            i = i.next
        i.next = head.next





head = Node("head",0)
a=Node("a",1)
b=Node("b",2)
c=Node("c",3)
d=Node("d",4)
e=Node("e",5)
f=Node("f",6)
g=Node("g",7)
h=Node("h",8)
i=Node("i",9)

qqq = queue()

qqq.put(a)
qqq.put(b)
qqq.put(c)
qqq.put(d)
qqq.put(e)
qqq.put(f)
qqq.put(g)
qqq.put(h)
qqq.put(i)
qqq.delete_next(i)
qqq.get()
qqq.get()
qqq.get()
qqq.get()
