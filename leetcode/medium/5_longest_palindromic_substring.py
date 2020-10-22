# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
# Example 4:
#
# Input: s = "ac"
# Output: "a"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
# Accepted
# 1,071,043
# Submissions
# 3,595,843


# Logic -- Brute Force (Works but O(n^3) time complexity)
# Get all substrings and check if each substring is a palindrome
# If yes then check if bigger than the current palindrome
# Return longest palindrome substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        lps = ''

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if substring == substring[::-1] and len(substring) > len(lps):
                    lps = substring

        return lps




# Logic 2 -- O(n^2) Time Complexity
# Iterate over the string
# Create a helper func which takes two arguments substring, left index and right index
# Then left decrements by 1 and right increments by 1 if they match
# Do this for 2 cases --
# Case 1 -- where there is not middle character "abba"
# Case 2 -- where there is a middle charater "abcba"
# And check for 2 cases start from the middle and go outwards and return palindrome
# Keep track of the longest palindromic substring and return it

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        lps = ''

        def expand_from_middle(s, left, right):
            if s == "" or left > right:
                return None
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(0, len(s)):
            pal1 = expand_from_middle(s, i, i)              #--> Case 1
            pal2 = expand_from_middle(s, i, i + 1)          #--> Case 2
            if len(pal1) > len(pal2) and len(pal1) > len(lps):
                lps = pal1
            elif len(pal2) > len(pal1) and len(pal2) > len(lps):
                lps = pal2

        return lps