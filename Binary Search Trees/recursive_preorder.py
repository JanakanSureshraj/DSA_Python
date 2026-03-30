# Recursive pre-order traversal 
from bst import BST
def pre_order_print(self, subtree): 
	if subtree is not None: 
		print(subtree.data, end=" ")
		self.pre_order_print(subtree.left)
		self.pre_order_print(subtree.right)

def print(self):
	self.pre_order_print(self.root)
	print(" ") 