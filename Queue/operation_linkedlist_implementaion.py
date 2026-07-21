# Queue Implementation using Linked List (Without Built-in Queue Functions)

# Node creation
class Node:
    def __init__(self, data):
        self.data = data  # Stores the value of node
        self.next = None  # Stores address of next node


front = None  # Points to first node of queue
rear = None   # Points to last node of queue


# Enqueue Operation (Insert Element)
def enqueue(element):
    global front, rear

    new_node = Node(element)  # Create a new node with given element

    if rear is None:  # If queue is empty
        front = rear = new_node  # Both front and rear point to new node

    else:
        rear.next = new_node  # Link old rear node to new node
        rear = new_node       # Move rear to new last node

    print(element, "inserted into queue")


# Dequeue Operation (Remove Element)
def dequeue():
    global front, rear

    if front is None:  # Checks if queue is empty
        print("Queue Underflow")
        return

    element = front.data  # Store front node data before removing

    front = front.next  # Move front pointer to next node

    if front is None:  # If queue becomes empty after deletion
        rear = None  # Reset rear pointer

    print(element, "removed from queue")


# Peek Operation (View Front Element)
def peek():

    if front is None:  # Checks if queue is empty
        print("Queue is Empty")
        return

    print("Front element:", front.data)  # Display first node data


# Display Queue Elements
def display():

    if front is None:  # Checks if queue is empty
        print("Queue is Empty")
        return

    temp = front  # Temporary pointer starts from front

    print("Queue elements:")

    while temp is not None:  # Traverse until last node
        print(temp.data, end=" ")  # Print current node data
        temp = temp.next  # Move to next node

    print()


# Check Queue Empty
def is_empty():

    if front is None:  # Queue is empty when front has no node
        return True

    else:
        return False


# Main Program
while True:

    print("\nQueue Operations")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Check Empty")
    print("6. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:

        value = int(input("Enter element: "))
        enqueue(value)  # Insert element at rear


    elif choice == 2:

        dequeue()  # Remove element from front


    elif choice == 3:

        peek()  # Display front element


    elif choice == 4:

        display()  # Display all queue elements


    elif choice == 5:

        if is_empty():  # Check whether queue is empty
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")


    elif choice == 6:

        print("Program Ended")
        break  # Exit program


    else:

        print("Invalid Choice")