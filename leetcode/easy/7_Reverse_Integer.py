# 7. Reverse Integer
# Easy
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
#
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
# Example 4:
#
# Input: x = 0
# Output: 0
#
#
# Constraints:
#
# -231 <= x <= 231 - 1


# Logic
# Reverse number by converting it to string
# Special case if the number is negative
# Then do a check on the reversed number if it falls in the

class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = (2 ** 31) - 1
        MIN_INT = (-2 ** 31)

        if x < 0:
            ret_num = int("-" + str(x)[1:][::-1])
        else:
            ret_num = int(str(x)[::-1])

        if ret_num <= MIN_INT:
            return 0
        elif ret_num > MAX_INT:
            return 0
        else:
            return ret_num
