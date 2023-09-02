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