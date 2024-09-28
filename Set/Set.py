'''
Problem Statement: Create a program that determines whether a piece of text has unique characters.
'''
# Linear Time complexity: O(n) is taken to complete execution of the following function.
def has_unique_characters(data):
    new_set = set(data)
    return len(data) == len(new_set):

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('data'))
print(has_unique_characters('python'))

'''Key Point'''
# Frozen Sets were introduced in Python 3.4 as a way to make immutable sets.
primary_colors = frozenset(["red", "blue", "yellow"])
# primary_colors.add("green") # Will throw AttributeError


