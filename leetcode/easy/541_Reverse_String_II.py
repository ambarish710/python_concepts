# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
#
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
#
#
#
# Example 1:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
#
# Input: s = "abcd", k = 2
# Output: "bacd"
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104


# Logic
# Create a empty string
# Create iteration variable which we will use to check if we have to reverse the string or not
# i position variable
# Iterate till i < len(s)
    # Get the substring
    # Check if we have to reverse it or not
    # Append it to t
# Return t


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = ""
        i = 0
        iteration = 0
        while i < len(s):
            if (iteration % 2) != 1:
                t += s[i:i + k][::-1]
            else:
                t += s[i:i + k]
            i += k
            iteration += 1
        return t
