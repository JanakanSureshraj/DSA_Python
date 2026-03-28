from bst import Node, BinarySearchTree

def insert(self, data, subtree):
    if subtree is None: 
        return BST.Node(data) # create a new node with the data and return it
    elif data < subtree.data:
        subtree.left = self.insert(data, subtree.left) # insert in the left subtree
        return subtree
    elif data > subtree.data:
        subtree.right = self.insert(data, subtree.right) # insert in the right subtree
        return subtree
    
def insert_recursivese(self, data):
    self.root = self.insert(data, self.root) # start the insertion from the root
    