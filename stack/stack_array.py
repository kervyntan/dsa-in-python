class Stack():

    def __init__(self, size, top):
        self.size = size
        self.data = [0]*size
        self.top = top
    
    def push(self, x):
        if self.top >= self.size - 1:
            print("Stack Overflow")
        else:
            self.top = self.top + 1
            self.data[self.top] = x
            print(self.data[self.top])

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            popped_data = self.data[self.top]
            self.data[self.top] = 0
            self.top = self.top - 1
            return popped_data
        
    def peek(self):
        if self.top == -1:
            print("Stack is empty.")
        else:
            print(self.data[self.top])

stack = Stack(3, -1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.data[0 : stack.top + 1])
print(stack.pop())
