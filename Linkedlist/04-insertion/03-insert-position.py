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

    
    def insertatposition(self, pos, data):
        new_node = Node(data)

        current = self.head
        index = 1

        while current:
            if index == pos - 1:
                new_node.next = current.next
                current.next = new_node
                return

            current = current.next
            index += 1
            current = current.next




# Creating linked list
ll = LinkedList()

# Inserting nodes
ll.insert_beginning(30)
ll.insert_beginning(20)
ll.insert_beginning(10)
ll.insert_beginning(5)
ll.insertatposition(2, 7)
# Display list
ll.display()