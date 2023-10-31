# Part 1: Create a BSTNode class
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)


# Part 2: Create a BST class
class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = []

    def __str__(self):
        if self.root == None:
            return "The tree is empty"
        else:
            self.output = ""
            self.print_tree(node=self.root)
            return self.output
        
    def __repr__(self):
        if self.root == None:
            return "The tree is empty"
        else:
            self.output = ""
            self.print_tree(node=self.root)
            return self.output
        
    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level+1)
            self.output += " " * 4 * level + "-> " + str(node.data) + "\n"
            self.print_tree(node.left, level + 1)
            
# Part 3: Add functionality to your BST class

if __name__ == "__main__":
    
  node1 = BSTNode("hello")
  print(node1)