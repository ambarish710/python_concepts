# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: 6
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:
#
# Input: nums = [-1,-2,-3]
# Output: -6
#
#
# Constraints:
#
# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000


# Logic
# Sort the array
# Check which is bigger in between
    # 1 -- (nums[-1] * nums[-2] * nums[-3]) three biggest elements
    # 2 -- (nums[0] * nums[1] * nums[-1]) two smallest and biggest element
        # The reason being the two smallest can be negative numbers
        # And -ve * -ve = +ve

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max((nums[0] * nums[1] * nums[-1]), (nums[-1] * nums[-2] * nums[-3]))