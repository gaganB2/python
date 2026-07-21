class Stack:

    def __init__(self, size):
        self.stack = [None] * size          # create fixed size empty array
        self.top = -1                       # top index, -1 means stack is empty
        self.size = size                    # store maximum capacity of stack

    def push(self, value):
        if self.top == self.size - 1:       # check if stack is full
            raise OverflowError("Stack is full")

        self.top += 1                       # move top to next available index
        self.stack[self.top] = value        # insert value at top position

    def pop(self):
        if self.is_empty():                 # check if stack has no elements
            raise IndexError("Stack is empty")

        value = self.stack[self.top]        # get current top value
        self.stack[self.top] = None         # clear removed position
        self.top -= 1                       # move top down, removing top logically

        return value                        # return removed value

    def peek(self):
        if self.is_empty():                 # check if stack has no elements
            raise IndexError("Stack is empty")

        return self.stack[self.top]         # return top value without removing

    def is_empty(self):
        return self.top == -1               # true when stack has no elements

    def get_size(self):
        return self.top + 1                 # number of elements currently in stack

    def display(self):
        for i in range(self.top, -1, -1):   # start from top and go down
            print(self.stack[i])


# Example usage

stack = Stack(5)

stack.push(10)                              # add 10
stack.push(20)                              # add 20
stack.push(30)                              # add 30

print("Top:", stack.peek())                 # see top element

print("Removed:", stack.pop())              # remove top element

print("Size:", stack.get_size())            # current number of elements

stack.display()                             # display stack from top to bottom