# KEY TAKEAWAY: 
'''If right subtree exists:
→ go right, then all the way left

Else:
→ go up, find first ancestor where you went left'''

def inorder_successor(self, data):
    curr = self.root
    successor = None
    
    while curr is not None:
        if data < curr.data:
            successor = curr
            curr = curr.left
        elif data > curr.data:
            curr.right
        else: #NODE FOUND
            if curr.right:
                temp = curr.right
                while temp.left:
                    temp=temp.left
                return temp
            return successor
        
        return successor #Returns none if no successor exists