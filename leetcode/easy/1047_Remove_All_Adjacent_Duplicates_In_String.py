# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
#
# We repeatedly make duplicate removals on S until we no longer can.
#
# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
#
#
#
# Example 1:
#
# Input: "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
#
#
# Note:
#
# 1 <= S.length <= 20000
# S consists only of English lowercase letters.



# Logic
# Use stack to sort this issue
# Check if last element on stack is equal to given char
    # Check till last 2 elements in stack are not equal
# Move forward




class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [S[0]]

        for i, char in enumerate(S[1:]):
            if stack == []:
                stack.append(char)
            else:
                if char == stack[-1]:
                    del stack[-1]
                    while len(stack) > 1 and stack[-1] == stack[-2]:
                        del stack[-1]
                else:
                    stack.append(char)

        return "".join(stack)