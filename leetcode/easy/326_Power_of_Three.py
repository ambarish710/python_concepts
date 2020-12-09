# Given an integer n, return true if it is a power of three. Otherwise, return false.
#
# An integer n is a power of three, if there exists an integer x such that n == 3x.
#
#
#
# Example 1:
#
# Input: n = 27
# Output: true
# Example 2:
#
# Input: n = 0
# Output: false
# Example 3:
#
# Input: n = 9
# Output: true
# Example 4:
#
# Input: n = 45
# Output: false
#
#
# Constraints:
#
# -231 <= n <= 231 - 1
#
#
# Follow up: Could you do it without using any loop / recursion?



# Logic
# Mathematical Approach
# What ever root of a number
    # Square Root -- math.log10(n)/math.log10(2)
    # Cube Root -- math.log10(n)/math.log10(3)
    # Fourth Root -- math.log10(n)/math.log10(4)
# And the way to check if a num is a float or int
    # if num % 1 == 0
        # print(“int”)
    # else:
        # print(“float”)



import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if (math.log10(n)/math.log10(3)) % 1 == 0:
            return True
        else:
            return False
