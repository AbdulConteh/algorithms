# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # creating an instance
# # first_node = Node(12)
# # second_node = Node(17)

# # # prints pointer of Node
# # print('First Node', first_node)
# # # prints data from Node
# # print('Second Node', second_node.data)
# # # prints the next Node in Singly Linked List 
# # print('First Node', first_node.next)

# class SLL:
# # setting the head of the SLL
#     def __init__(self, head):
#         self.head = head 

#     def add(self, data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node 
#             return self
#         # runner lets you run through all of Nodes 
#         runner = self.head
#         while runner.next:
#             runner = runner.next
#         runner.next = new_node
#         return self

# # display all 
#     def display(self):
#         runner = self.head
#         node = 1
#         while runner:
#             print(f'This ia Node {node}. It has a data/value of {runner.data}')
#             node += 1
#             runner = runner.next
#         return self

# list = SLL(Node(10))
# print(list.head.data)

# list.add(13).add(24).add(92).add(76).add("Dinner is ready!!")
# list.display()
# print(list.head.next.data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None 

    def new_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self

list = SLL(Node(1))


