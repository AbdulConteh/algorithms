class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        pass

class BST:
    def __init__(self, root):
        self.root = root 

#Add Node 
    def add(self, data):
        runner = self.root
        # create a node that contians data / value
        new_node = Node(data)
        # create a while loop / stops at last Node (None/null)
        while runner:
            # is the new data < or > than new code 
            if data > runner.data:
                # if there is another branch
                if runner.right:
                    runner = runner.right
                # if this is not a new branch 
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

#Node Search 
    def search(self, data):
        monkey = self.root
        while monkey:
            # check to see if data is there
            if data > monkey.data:
                monkey = monkey.right
            elif data < monkey.data:
                monkey = monkey.left
            elif data == monkey.data:
                return monkey, "I have found it? The Node!!!! Muahaha!!"
        return "Sorry these are not the nodes you are looking for"

new_bst = BST(Node(13))

print(new_bst, "This is our Object")
print(new_bst.root.data, "The Root Node Data / Value")

new_bst.add(5).add(10).add(9).add(18).add(44)

print(new_bst.root.right.data)
print(new_bst.search(72))

print(new_bst.root)