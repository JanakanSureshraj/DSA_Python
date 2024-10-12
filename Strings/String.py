"""
Medium
Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3
Explanation: The longest substring is "abc", with the length of 3.
"""

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


"""
Algorithm:
Initialize a set to keep track of characters in the current window.
Initialize two pointers left = 0 and right = 0 for the window.
Traverse the string with the right pointer.
If the character at s[right] is not in the set, add it to the set and update the maximum length of the window.
If s[right] is in the set, move the left pointer to the right and remove s[left] from the set until there are no duplicates.
Return the maximum length found.
"""

"""
Time Complexity:O(n), where n is the length of the string. Each character is added and removed from the set at most once.
Space Complexity: O(min(m, n)), where m is the size of the character set (like 26 for English lowercase letters),
and n is the length of the string.
"""
