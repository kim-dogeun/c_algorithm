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

    def insert_node_between(self,node1, node2,node3):
        node2.next = node3
        node1.next = node2
        node2.before = node1
        node3.before = node2
    
    
head = Node("head")
tail = Node("tail")
a = Node('a')
b = Node('b')
c = Node('c')
dublik = dubblelinked()
dublik.insert_node_between(head,a,tail)
dublik.insert_node_between(a,b,tail)
dublik.insert_node_between(b,c,tail)
dublik.get_nodes()
