class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self, head):
        self.head = head

    def funGame(self, data):
        if (self.head == None):
            return True
        

    def display(self):
        runner = self.head
        node = 1
        while runner:
            print(f'This ia Node {node}. It has a data/value of {runner.data}')
            node += 1
            runner = runner.next
        return self