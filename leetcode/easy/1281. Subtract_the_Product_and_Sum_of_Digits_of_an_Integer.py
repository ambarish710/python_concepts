# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#
#
# Example 1:
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
# Example 2:
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21
#


# Logic
# Create a list of ints in the nums
# Create product and sum of the ints
# Return product - sum


import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        elements = [int(item) for item in str(n)]
        product = 1
        nsum = 0
        for element in elements:
            product *= element
            nsum += element
        return product - nsum