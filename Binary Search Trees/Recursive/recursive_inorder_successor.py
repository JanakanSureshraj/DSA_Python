# Find the inorder successor of a given node in a BST recursively
from bst import BST

def r_inorder_successor(self, value, subtree, succ):
    if subtree is None:
        return succ
    
    if value < subtree.value:
        # potential successor
        return self.r_inorder_successor(value, subtree.left, subtree)
    
    elif value > subtree.value:
        return self.r_inorder_successor(value, subtree.right, succ)

    else:
        # Node found
        if subtree.right is not None:
            # find leftmost in right subtree
            curr = subtree.right
            while curr.left:
                curr = curr.left
            return curr
        return succ


def inorder_successor(self, value):
    result = self._r_inorder_successor(value, self.root, None)
    return result.value if result else None