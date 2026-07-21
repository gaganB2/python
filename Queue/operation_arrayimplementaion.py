# Queue Implementation using Array (Without Built-in Queue Functions)

MAX = 5  # Maximum size of queue

queue = [0] * MAX  # Creating an array to store queue elements

front = -1  # Points to the first element of queue
rear = -1   # Points to the last element of queue


# Enqueue Operation (Insert Element)
def enqueue(element):
    global front, rear

    if rear == MAX - 1:  # Checks if rear reached the last index of array
        print("Queue Overflow")
        return

    if front == -1:  # If queue is empty, set front to first index
        front = 0

    rear = rear + 1  # Move rear to next position
    queue[rear] = element  # Insert element at rear position

    print(element, "inserted into queue")


# Dequeue Operation (Remove Element)
def dequeue():
    global front, rear

    if front == -1:  # Checks if queue is empty
        print("Queue Underflow")
        return

    element = queue[front]  # Store front element before removing it

    front = front + 1  # Move front to next element

    if front > rear:  # If front crosses rear, queue has become empty
        front = -1  # Reset front
        rear = -1    # Reset rear

    print(element, "removed from queue")


# Peek Operation (View Front Element)
def peek():

    if front == -1:  # Checks if queue is empty
        print("Queue is Empty")
        return

    print("Front element:", queue[front])  # Display element at front index


# Display Queue Elements
def display():

    if front == -1:  # Checks if queue is empty
        print("Queue is Empty")
        return

    i = front  # Start displaying from front position

    print("Queue elements:")

    while i <= rear:  # Continue until rear position is reached
        print(queue[i], end=" ")  # Print current queue element
        i = i + 1  # Move to next index

    print()


# Check Queue Empty
def is_empty():

    if front == -1:  # Queue is empty when front is -1
        return True

    else:
        return False


# Check Queue Full
def is_full():

    if rear == MAX - 1:  # Queue is full when rear reaches last index
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
    print("6. Check Full")
    print("7. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:

        value = int(input("Enter element: "))
        enqueue(value)  # Call insert operation


    elif choice == 2:

        dequeue()  # Call delete operation


    elif choice == 3:

        peek()  # Call front element operation


    elif choice == 4:

        display()  # Display all queue elements


    elif choice == 5:

        if is_empty():  # Check if queue has no elements
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")


    elif choice == 6:

        if is_full():  # Check if queue has reached maximum size
            print("Queue is Full")
        else:
            print("Queue is Not Full")


    elif choice == 7:

        print("Program Ended")
        break  # Exit the program


    else:

        print("Invalid Choice")  # Handles invalid menu input