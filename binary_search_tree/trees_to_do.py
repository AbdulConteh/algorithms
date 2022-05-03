from turtle import left, right


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self, root):
        self.root = root

# add
    def add(self, data):
        # create a runner that contains root
        runner = self.root
        # create new node that has Node data
        new_node = Node(data)
        # create a while loop that sets a stop point 
        while runner:
            # is data < or > new_data?
            if data > runner.data:
                if runner.right:
                    runner = runner.right
                else:
                    runner.right = new_node
                    return self
            else:
                if runner.left: 
                    runner = runner.left
                else:
                    runner.left = new_node
                    return self
        return self

# contains
    def search(self, data):
        runner = self.root
        while runner:
            if data > runner.data:
                runner = runner.right
            elif data < runner.data:
                runner = runner.left
            elif data == runner.data:
                return runner, "found ya"
        return "No node here"

# min
    def min(self, root):
        runner = self.root
        min = self.root.data
        while runner.left:
            if runner.left.data < min:
                min = runner.left.data
            return runner.left
        return min

# max
    def max(self):
        runner = self.root
        max = self.root.data
        print(max)
        if runner.right:
            while runner.right:
                if runner.right.data > max:
                    max = runner.right.data
                return runner.right
            print(max)
        return max


new_bst = BST(Node(50))

print(new_bst.root.data)

new_bst.add(40).add(60).add(32).add(90).add(39)

print(new_bst.root.left.data)
print(new_bst.search(32))

print(new_bst.max)
print(new_bst.min)
