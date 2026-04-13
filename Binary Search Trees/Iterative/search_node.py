def search(self, data): 
    if self.root is None: 
        return None 
    
    curr = self.root
    while curr is not None: 
        if data < curr.data:
            curr = curr.left
        elif data > curr.data: 
            curr = curr.right
        else: 
            return curr # found the node with the data

