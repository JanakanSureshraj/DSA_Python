# Minimum value in a BST

def minimum_element(self):
    if self.root is None: 
        return None
        
    curr = self.root 
    while curr.left is not None:
        curr = curr.left 
    return curr.data