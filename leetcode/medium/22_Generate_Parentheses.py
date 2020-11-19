# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8


# Logic
# Classic example of recursion + backtracking...
# You write a method which takes openbracket, closingbracket count, max number of brackets allowed and s == current temp variable
# Have a few basic checks and boom you're done
    # Basic check 1 --> if closingbrackets == n:
        # Add the current list (conv to string) and put it inside a list
        # Used list bcoz lists are immutable and strings aren't
    # if openbrackets > closingbrackets:
        # Add a new closing bracket
        # recursively call the same function or self again by incrementing closing bracket
        # pop the recently added bracket --> This comes as part of backtracking
    # if openbrackets < n:
        # Add a new opening bracket
        # recursively call the same function or self again by incrementing opening bracket
        # pop the recently added bracket --> This comes as part of backtracking


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []

        def backtracking(openbrackets, closingbrackets, n, s=[]):

            if closingbrackets == n:
                self.output.append("".join(s))
                return

            else:
                if openbrackets > closingbrackets:
                    s.append(")")
                    backtracking(openbrackets, closingbrackets + 1, n, s)
                    s.pop()

                if openbrackets < n:
                    s.append("(")
                    backtracking(openbrackets + 1, closingbrackets, n, s)
                    s.pop()

            return

        backtracking(openbrackets=0, closingbrackets=0, n=n)

        return self.output