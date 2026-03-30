# Find height of a BST recursively 
from bst import BST

def height(self, subtree):
    if subtree is None: 
        return 0
    return max(self.height(subtree.left), self.height(subtree.right)) + 1

def r_height(self):
    return self.height(self.root)