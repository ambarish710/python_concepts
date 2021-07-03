# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Example 3:
#
# Input: nums = [0]
# Output: 0
# Example 4:
#
# Input: nums = [-1]
# Output: -1
# Example 5:
#
# Input: nums = [-100000]
# Output: -100000
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105
#
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



# Logic
# Way 1 normal brute force logic with double for loops

# Way 2
# Greddy approach
# The algorithm is general and straightforward: iterate over the array and update at each step the standard set for such problems:
# current element
# current local maximum sum (at this given point)
# global maximum sum seen so far.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Way 1
                if len(nums) == 1:
                    return nums[0]

                max_sum = float("-inf")

                for i in range(len(nums)):
                    for j in range(i+1, len(nums)+1):
                        temp_sum = sum(nums[i:j])
                        if temp_sum > max_sum:
                            max_sum = temp_sum

                return max_sum


        # Way 2
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum