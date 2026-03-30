# Count nodes at a specified height in a BST recursively
from bst import BST
def count_nodes_at_height(self, subtree, height):
    if subtree is None: 
        return 0

    if height == 0:
        return 1

    return self.count_nodes_at_height(subtree.left, height - 1) + self.count_nodes_at_height(subtree.right, height - 1)

def r_count_nodes_at_height(self, height):
    return self.count_nodes_at_height(self.root, height)
