# Recursive in-oder traversal

def in_order_print(self, subtree): 
	if subtree is not None:
		self.in_order_print(subtree.left)
		print(subtree.data, end=" ")
		self.in_order_print(subtree.right)

def print(self): 
		self.in_order_print(self.root)
		print("")  