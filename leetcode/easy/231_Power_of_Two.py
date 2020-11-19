# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2x.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:
#
# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:
#
# Input: n = 3
# Output: false
# Example 4:
#
# Input: n = 4
# Output: true
# Example 5:
#
# Input: n = 5
# Output: false
#
#
# Constraints:
#
# -231 <= n <= 231 - 1


# Logic
# Initialize 2 ints one is the iteration variable and other is the value variable
# Iterate till value variable less than required n
# Increment iteration variable by 1
# Post that check if val == n, if yes return true
# Else return false



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        val = 0
        while val < n:
            val = 2 ** i
            i += 1

        if val == n and val != 0:
            return True
        else:
            return False