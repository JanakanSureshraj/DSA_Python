'''
Problem Statement: Create a function to find the second smallest item in a list of integers.
    - The input list is unsorted
    - Second smallest item can be at any position
    - List might have just one item, in that case, the function should return None
    - Assume no duplicates are present
'''

# Timsort Algorithm: hybrid sorting algorithm that combines two other algorithms: Merge Sort and Insertion Sort.
# Time Complexity= O(n log n)

def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[1]
print(find_second_smallest([5, 8, 3, 2, 6]))


# Custom Algorithm 
# Time Complexity = O(n) because we only iterate through the list once.
# This can be considered a variant of Linear Search because we are not looking for a specific value, but are using linear traversal to update variables.

def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    # Set the smallest and second smallest numbers to positive infinity.
    smallest = float('inf') 
    second_smallest =float('inf')
    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest

print(find_second_smallest_v2([5, 8, 3, 2, 6]))


'''
--More on this--
'''
# Linear Search- simple searching technique where you go through each element in a list (or array) one-by-one, from start to end, until you find what you're looking for or finish checking all elements.
# The time it takes for the algorithm to execute increases as the size of input increases.
# This means that, in the worst case, you have to examine every single element to find the result.
my_list = [8, 5, 0, 3]
ITEM = 7
def search(item, listy):
    for element in listy:
        if element == item:
            return True
    return False
print(search(ITEM, my_list))

# ITEM_INDEX = my_list.index(ITEM) returns the index, but this is linear search too.

# SORT a list- Python uses the Timsort algorithm
print(sorted(my_list, reverse=True))

student_grades = [('Sarah', 89), ('Rebecca', 82), ('Matt', 91)]
print(sorted(student_grades)) # Sorts alphabetically by name (default)
print(sorted(student_grades, key=lambda x:x[1], reverse=True)) # Sort by grade

