# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s split it in the maximum amount of balanced strings.
#
# Return the maximum amount of splitted balanced strings.
#
#
#
# Example 1:
#
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:
#
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3:
#
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# Example 4:
#
# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s[i] = 'L' or 'R'



# Logic
# Keep a "R" count variable
# Iterate over the chars in s
# If char is "R" increment r_count by 1
# Else decrement r_count by 1
# If r_count == 0 increment total_split_string += 1
    # Which number of R is == number of L
# Return total_split_string


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        total_split_string = 0

        for char in s:
            if char == "R":
                # char is an R increment r_count by 1
                r_count += 1
            else:
                # char is an L decrement r_count by 1
                r_count -= 1

            if r_count == 0:
                total_split_string += 1

        return total_split_string
