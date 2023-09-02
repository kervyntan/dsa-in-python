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

stack = Stack(3, -1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.data[0 : stack.top + 1])
