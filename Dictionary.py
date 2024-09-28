'''
Problem Statement: Create a function that takes in a dictionary and creates a new dictionary without empty values.
    - Should not modify the original dictionary
'''

# Time Complexity of the below solution= linear or O(n) and this means as the input grows in size, so will the time it takes to run the algorithm.
user_preferences ={
    "timezone":"GMT",
    "language":"English",
    "notifications":None,
    "currency":"USD",
    "theme":None
    }

    def update_preferences(user_pref):
    updated_preferences = {}
    for key, value in user_pref.items():
        if value is not None:
            updated_preferences[key] = value
    return updated_preferences

print(update_preferences(user_preferences))

# The above implementation can be simplified by using dictionary comprehensions.
# Dictionary comprehensions provide a concise way to create an iterable object.

def update_preferences_v2(user_pref):
    return {key: value for key, value in user_pref.items() if value is not None}

# Four components in this comprehension
# 1- Set the key: key remains the same before the : 
# 2- Set the value: value remains the same too, just remove those that do not meet the condition
# 3- Iterable: user_pref.items() 
# 4- Condition: keep each key-value pair if the condition is met
