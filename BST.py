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
            self.print_tree(node.right, level + 1)
            self.output += " " * 4 * level + "-> " + str(node.data) + "\n"
            self.print_tree(node.left, level + 1)

    # Part 3: Add functionality to your BST class
    def add(self, data):
        if not isinstance(data, BSTNode) and not isinstance(data, int):
            raise ValueError("Input must be an int or a BSTNode")

        if isinstance(data, int):
            data = BSTNode(data)

        if self.root is None:
            self.root = data
            self.contents.append(data.data)
            return

        if data.data in self.contents:
            return

        self.add_node(self.root, data)
        self.contents.append(data.data)

    def add_node(self, node, new_node):
        if new_node.data < node.data:
            if node.left is None:
                node.left = new_node
            else:
                self.add_node(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self.add_node(node.right, new_node)

    def remove(self, remove_value):
        if not isinstance(remove_value, BSTNode) and not isinstance(remove_value, int):
            raise ValueError("Input must be an int or a BSTNode")

        if isinstance(remove_value, BSTNode):
            remove_value = remove_value.data

        if remove_value not in self.contents:
            raise ValueError("Value not found in tree")

        self.remove_node(self.root, remove_value)

    def remove_node(self, current, remove_value, prev=None):
        if current is None:
            return

        if current.data == remove_value:
            if current.left is None and current.right is None:
                if prev is None:
                    self.root = None
                elif prev.left == current:
                    prev.left = None
                else:
                    prev.right = None
            elif current.left is None:
                if prev is None:
                    self.root = current.right
                elif prev.left == current:
                    prev.left = current.right
                else:
                    prev.right = current.right
            elif current.right is None:
                if prev is None:
                    self.root = current.left
                elif prev.left == current:
                    prev.left = current.left
                else:
                    prev.right = current.left
            else:
                self.nodes = []
                self.traverse_tree(current.right)
                self.nodes.remove(remove_value)
                self.contents.remove(remove_value)
                if prev is None:
                    self.root = BSTNode(self.nodes.pop(len(self.nodes) // 2))
                elif prev.left == current:
                    prev.left = BSTNode(self.nodes.pop(len(self.nodes) // 2))
                else:
                    prev.right = BSTNode(self.nodes.pop(len(self.nodes) // 2))
                for node in self.nodes:
                    self.add(node)
        elif remove_value > current.data:
            self.remove_node(current.right, remove_value, prev=current)
        else:
            self.remove_node(current.left, remove_value, prev=current)

    def traverse_tree(self, node):
        if node is not None:
            self.traverse_tree(node.right)
            self.nodes.append(node.data)
            self.traverse_tree(node.left)


if __name__ == "__main__":
    node1 = BSTNode(3)
    # print(node1)  # 3

    node2 = BSTNode(4, left=node1)
    # print(node2)  # 4
    # print(node2.left)

    node3 = BSTNode()
    # print(node3)  # None
    node3.data = 5
    # print(node3)  # 5

    bst = BST()
    print(bst)

    bst.root = node2
    print(bst)

    node2.right = node3
    print(bst)

    # create tree from image
    node8 = BSTNode(8)
    node3 = BSTNode(3)
    node10 = BSTNode(10)
    node1 = BSTNode(1)
    node6 = BSTNode(6)
    node14 = BSTNode(14)
    node4 = BSTNode(4)
    node7 = BSTNode(7)
    node13 = BSTNode(13)

    bst = BST()
    bst.add(node8)
    bst.add(node3)
    bst.add(node10)
    bst.add(node1)
    bst.add(node6)
    bst.add(node14)
    bst.add(node4)
    bst.add(node7)
    bst.add(node13)
    print(bst)
