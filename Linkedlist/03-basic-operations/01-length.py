class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    
    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current=current.next
        return count


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

ll = Linkedlist()
ll.head = node1
print(ll.length())

