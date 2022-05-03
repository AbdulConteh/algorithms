class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# return value of node 
first_node = Node(10)
print(first_node)
print("first node", first_node.data) 


class SLL:
    def __init__(self, head):
        self.head = head

# remove front
    def remove(self):
        if (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
            return self

# Add Front
    def front(self, data):
        new_front = Node(data)
        if self.head == None:
            new_front.next = self.head
        self.head = new_front
        return self

# display all 
    def display(self):
        runner = self.head
        node = 1
        while runner:
            print(f'This ia Node {node}. It has a data/value of {runner.data}')
            node += 1
            runner = runner.next
        return self

list = SLL(Node(85))
# list.front("second node:").front(32)
list.front("second node:").front(32)
# print(list.head)
print(list.head.data)

