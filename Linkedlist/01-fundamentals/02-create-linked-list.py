class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    pass
    def __init__(self):
        self.head = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

ll = Linkedlist()
ll.head = node1

newnode = Node(40)
current = ll.head

while current.next is not None:
    current = current.next
current.next = newnode
print(current.next.data)