# Count the nodes in a BST recursively 
from bst import BST

def count_nodes(self, subtree):
	if subtree is None:
		return 0
	return 1 + (self.count_nodes(subtree.left)) + (self.count_nodes(subtree.right))

def r_count(self):
	return self.count_nodes(self.root)  