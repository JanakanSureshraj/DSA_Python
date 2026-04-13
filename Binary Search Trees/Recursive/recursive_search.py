# Recursive search in a binary search tree is a common operation that allows us to find a specific value in the tree. 
# Below is an implementation of a binary search tree along with a recursive search function.
from bst import Node, BinarySearchTree

def search(self, data, subtree): 
        if subtree is None: 
            return None
        else: 
            if data < subtree.data: 
                return self.search(data, subtree.left)
            elif data > subtree.data:
                return self.search(data, subtree.right)
            else:
                return subtree # data is already in the tree, return the node (node found)
            
def search_recursive(self, data): 
        return self.search(data, self.root)
    
    
# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    # Assume we have a method to insert values into the BST
    # bst.insert(10)
    # bst.insert(5)
    # bst.insert(15)

    # Now we can search for values
    result = bst.search_recursive(5)
    if result:
        print(f"Value {result.data} found in the tree.")
    else:
        print("Value not found in the tree.")