class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.before = None
    
class dubblelinked:
    def __init__(self):   
        head.next = tail
        head.before = head
        tail.next = tail
        tail.before = head
        self.head = head
        self.tail = tail
    
    def get_nodes(self):
        i = self.head
        while(i != self.tail):
            print(i.key)
            i = i.next
        print(i.key)

    def insert_node_next(self,node1):
        i = self.head
        while(i != self.tail.before):
            i = i.next
        
        i.next = node1
        node1.next = self.tail
        node1.before = i
        self.tail.before = node1


class stack(dubblelinked):
    def __init__(self):
        dubblelinked.__init__(self)

    def push(self,node2):
        self.insert_node_next(node2)
    
    def pop(self):
        i = self.head
        while(i != self.tail.before):
            i = i.next
        i.before.next = self.tail
        self.tail.before = i.before





head = Node("head")
tail = Node("tail")
a= Node('a')
b=Node('b')
c=stack()
c.push(a)
c.get_nodes()
c.pop()
c.get_nodes()