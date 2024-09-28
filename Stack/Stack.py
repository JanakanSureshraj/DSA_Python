'''
Problem Statement: Develop a function that determines whether a piece of text has matching paranthesis.
    - The opening paranthesis ( should come before the closing paranthesis ) for it to be a match
    - Each opening is also closed
    - There may be other letter/s before or after each of the paranthesis
'''

# Time Complexity of this solution = O(n): the algorithm processes each character in the string exactly once.

from collections import deque

def check_matching_paranthesis(s):
    stack = deque()

    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

# Valid Input
print(check_matching_paranthesis("()"))
print(check_matching_paranthesis("(hi there)"))
print(check_matching_paranthesis("(hell)o"))
print(check_matching_paranthesis("((yes)) yes"))
# Invalid Input
print(check_matching_paranthesis("(hi(there"))
print(check_matching_paranthesis("()ok)"))
print(check_matching_paranthesis("((increment)"))
print(check_matching_paranthesis(")linkedin()"))        

# Example of execution:
'''
Input: "((increment)"
Stack starts empty: [].
Encounter (: Stack becomes ['('].
Encounter (: Stack becomes ['(', '('].
Encounter i, n, c, r, e, m, e, n, t: Ignore.
Encounter ): Pop the stack, Stack becomes ['('].
Stack is not empty (still has one ( left), so return False.
'''
