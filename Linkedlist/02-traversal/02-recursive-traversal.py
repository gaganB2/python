class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    
    def __init__(self):
        self.head = None


    def traverse(self, current):
        if current is None:
            return
        print(current.data)
        self.traverse(current.next)



node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

ll = Linkedlist()
ll.head = node1
ll.traverse(ll.head)

