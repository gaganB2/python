# Professional version
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        # New node points to current head
        new_node.next = self.head

        # Move head to the new node
        self.head = new_node

    # Display linked list
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Creating linked list
ll = LinkedList()

# Inserting nodes
ll.insert_beginning(30)
ll.insert_beginning(20)
ll.insert_beginning(10)
ll.insert_beginning(5)

# Display list
ll.display()





'''My version
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    
    def __init__(self):
        self.head = None

    def insert_beginning(self, node):
        # i have to add node and node.next should be pointing to head then head should be on new node

        
        node.next = self.head
        self.head = node
        return node.data
    
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
new_node = Node(5)

node1.next = node2
node2.next = node3

ll = Linkedlist()
ll.head = node1
print(ll.insert_beginning(new_node))
print(ll.display())
'''