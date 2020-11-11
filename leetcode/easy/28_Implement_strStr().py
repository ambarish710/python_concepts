# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
#
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:
#
# Input: haystack = "", needle = ""
# Output: 0
#
#
# Constraints:
#
# 0 <= haystack.length, needle.length <= 5 * 104
# haystack and needle consist of only lower-case English characters.


# Logic
# Cover the corner cases wherein if not needle and haystack return 0
# If len(needle) > len(haystack) then return -1
# Else: Iterate over haystack and check haystack[i:i+needle_len] == needle
        # Then return i (which is the index currently started on)
# Else return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle and not haystack:
            return 0

        if len(needle) > len(haystack):
            return -1

        compare_len = len(needle)
        for i, char in enumerate(haystack):
            if haystack[i:i + compare_len] == needle:
                return i
        else:
            return -1
