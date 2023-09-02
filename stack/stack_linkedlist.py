# Front of the linkedlist is the top of the stack

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node_to_be_added = Node(data)
        if self.size == 0:
            self.top = node_to_be_added
            # node_to_be_added.next = None
        else:
            node_to_be_added.next = self.top
            self.top = node_to_be_added
        self.size += 1
        print(node_to_be_added.data)
    
    def pop(self):
        if self.size == 0:
            print("Stack is empty.")
            return
        else:
            self.size = self.size - 1
            node = self.top
            self.top = node.next
            node.next = None
            print(node.data)
            return node
    
    def peek(self):
        if self.size == 0:
            print("Stack is empty.")
            return
        else:
            print(self.top.data)
            return self.top
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.peek()
# stack.pop()
# stack.pop()
# stack.pop()