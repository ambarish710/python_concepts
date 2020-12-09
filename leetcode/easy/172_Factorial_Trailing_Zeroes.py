# Given an integer n, return the number of trailing zeroes in n!.
#
# Follow up: Could you write a solution that works in logarithmic time complexity?
#
#
#
# Example 1:
#
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
#
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:
#
# Input: n = 0
# Output: 0
#
#
# Constraints:
#
# 1 <= n <= 104


# Logic
# Calculate the factorial of that num
# Convert it to num and traverse it in reverse direction
# And count the number of 0's


class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 1
        for i in range(1, n + 1):
            total *= i

        zeros = 0
        for char in reversed(str(total)):
            if char == "0":
                zeros += 1
            else:
                break

        return zeros
