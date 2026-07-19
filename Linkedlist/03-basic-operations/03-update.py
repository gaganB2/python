class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    
    def __init__(self):
        self.head = None

    # update node func
    # we need index and node 
    def update(self, position, value):
        current = self.head #points to first node
        # now we need to track using index
        index = 1 #which will go until position
        while current is not None:
            
            if index == position:
                current.data = value
                print("hi",current.data)
                break
            current = current.next
            index += 1
        # 
    




node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4


ll = Linkedlist()
ll.head = node1

ll.update(2,5)

print(node2.data)