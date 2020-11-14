# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


# Logic
# Keep the count of elements in list s in a dict scount
# Keep the count of elements in list t in a dict tcount
# Compare dicts
# If equal return true if not return false


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = defaultdict(int)
        tcount = defaultdict(int)

        for char in s:
            scount[char] += 1

        for char in t:
            tcount[char] += 1

        if tcount == scount:
            return True
        else:
            return False
