# Maximum element in BST

def maximum_element(self):
    if self.root is None: 
        return None
    
    curr = self.root
    while curr.right is not None:
        curr = curr.right
    return curr.data