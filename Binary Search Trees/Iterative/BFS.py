# Breadtth-First implementation of a Binary Search Tree

import queue 

def print_bst(self):
    nodes = queue.Queue()

    if self.root is not None:
        nodes.put(self.root)

    while not nodes.empty():
        curr = nodes.get()

        if curr.left:
            nodes.put(curr.left)
        if curr.right:
            nodes.put(curr.right)
        
        print(curr.data, end = " ")