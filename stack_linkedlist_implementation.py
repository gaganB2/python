class Stack:

    class Node:
        def __init__(self, value):
            self.value = value          # store data
            self.next = None            # point to next node


    def __init__(self):
        self.top = None                # top points to first node
        self.count = 0                 # track size


    def push(self, value):
        new_node = self.Node(value)    # create new node

        new_node.next = self.top       # new node points to old top

        self.top = new_node            # move top to new node

        self.count += 1                # increase size


    def pop(self):
        if self.is_empty():            # check if stack is empty
            raise IndexError("Stack is empty")

        value = self.top.value         # get top value

        self.top = self.top.next       # move top to next node

        self.count -= 1                # decrease size

        return value                   # return removed value


    def peek(self):
        if self.is_empty():            # check empty
            raise IndexError("Stack is empty")

        return self.top.value          # return top value only


    def is_empty(self):
        return self.top is None        # empty when top points to nothing


    def size(self):
        return self.count              # return number of nodes


    def display(self):
        current = self.top             # start from top

        while current:
            print(current.value)
            current = current.next     # move to next node


# Example

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top:", stack.peek())

print("Removed:", stack.pop())

print("Size:", stack.size())

stack.display()