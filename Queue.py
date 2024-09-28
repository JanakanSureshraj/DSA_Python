'''
Problem Statement: Genereate binary numbers from 1 to n.
    - n being the input and the limit
'''
# Given a number n, the program generates binary numbers from 1 to n as strings and prints them in sequence.
# For example, if n = 8, the binary numbers will be:
# 1
# 10
# 11
# 100
# 101   
# 110
# 111
# 1000

# There's a pattern here, 1 or 0 is being appended to the previous binary number.

# Breadth-First Search (BFS) approach
# The time complexity is O(n) because we only loop through the list once, generating n binary numbers.

from collections import deque

def print_binary_numbers(n):
    if n <= 0:
        return

    queue = deque()
    queue.append(1)

    for i in range(n):
        binary = queue.popleft()
        print(binary)
        queue.append(binary * 10)
        queue.append(binary * 10 + 1)

print_binary_numbers(1)
print()

print_binary_numbers(2)
print()

print_binary_numbers(5)
print()

print_binary_numbers(8)
print()

print_binary_numbers(10)
print()

'''
Breadth-First Search (BFS) is a method used to explore nodes and edges of a graph (or tree) systematically.
In simpler terms, it’s like exploring the layers or levels of a structure one-by-one.

How Does BFS Work in Programming?



BFS uses a queue data structure to keep track of nodes (or points) that need to be explored. Here’s a step-by-step breakdown of how BFS works:

1- Start from a node (or point).
2- Add it to the queue.
3- Explore all its neighbors (nodes or points directly connected to it).
4- Add these neighbors to the queue.
5- Remove the current node from the queue and move to the next node in the queue.
6- Repeat the process until the queue is empty.
'''
