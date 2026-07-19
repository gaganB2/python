class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)

        # New node points to current head
        new_node.next = self.head

        # Move head to the new node
        self.head = new_node

    # Insert a new node at the end
    def insert_end(self, data):
        if self.head is None:
            self.head = new_node
            return
        new_node = Node(data)
        current = self.head
        # I have to loop until last node
        while current.next:
            current = current.next
                
        current.next = new_node
            

        

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
ll.insert_end(40)
# Display list
ll.display()