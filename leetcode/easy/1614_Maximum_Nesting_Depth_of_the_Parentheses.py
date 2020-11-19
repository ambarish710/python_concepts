# A string is a valid parentheses string (denoted VPS) if it meets one of the following:
#
# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:
#
# depth("") = 0
# depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.
#
# Given a VPS represented as string s, return the nesting depth of s.
#
#
#
# Example 1:
#
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.
# Example 2:
#
# Input: s = "(1)+((2))+(((3)))"
# Output: 3
# Example 3:
#
# Input: s = "1+(2*3)/(2-1)"
# Output: 1
# Example 4:
#
# Input: s = "1"
# Output: 0
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
# It is guaranteed that parentheses expression s is a VPS.



# Logic
# Use Stack
# Iterate over the string
    # If you encounter "(". Store the opening bracket on the stack
    # If you encounter ")" check the last element on the stack. And check if its "(".
    # Update the depth variable which was initialized to 0.
        # If len(stack) > depth then depth = len(stack)
    # Perform stack.pop
# Return depth


class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0

        for char in s:
            if char == "(":
                stack.append("(")
            if char == ")" and stack[-1] == "(":
                if len(stack) > depth:
                    depth = len(stack)
                stack.pop()

        return depth