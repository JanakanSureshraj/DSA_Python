# Print nodes within a range in a BST recursively 
def print_between(self, min, max, subtree):
	if subtree is None:
		return
	if min < subtree.data:
		self.print_between(min, max, subtree.left)

	if min <= subtree.data <= max:
		print(subtree.data, end=" ")

	if max > subtree.data:
		self.print_between(min, max, subtree.right)

def r_print_between(self, min, max):
	self.print_between(min, max, self.root)
	print()