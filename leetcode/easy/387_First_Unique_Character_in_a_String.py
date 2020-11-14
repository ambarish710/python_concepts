# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
# Note: You may assume the string contains only lowercase English letters.
#


# Logic
# Use python inbuilt method Counter to count the occurences of chars in the string s
# Iterate over counter dict and get the char whose val or occurence count == 1
# Return the index of that char
# Else return -1
# use python for else wisely with break condition



from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurence_dict = Counter(s)

        for key, val in occurence_dict.items():
            if val == 1:
                char = key
                break
        else:
            return -1

        return s.index(char)