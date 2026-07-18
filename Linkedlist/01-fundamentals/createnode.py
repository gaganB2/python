class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1.data)
print(node1.next)

print(node1.next.data)
print(node1.next.next)

print(node1.next.next.data)
print(node1.next.next.next)

print(node1.next.next.next.data)
print(node1.next.next.next.next)

print("\n")

print(node1.data)
print(node1.next)

print(node2.data)
print(node2.next)

print(node3.data)
print(node3.next)

print(node4.data)
print(node4.next)
