# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
# Constraints:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7]
#
#
# .

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #         # Corner Cases
        #         if len(nums) == 1:
        #             if nums[0] == k:
        #                 return 1
        #             else:
        #                 return 0

        # Works but not an optimal solution (TC --  O(n^2))
        #         total_count = 0
        #         for i in range(0, len(nums)):
        #             sum = nums[i]
        #             if sum == k:
        #                     total_count += 1
        #             for j in range(min(i+1, len(nums)), len(nums)):
        #                 sum += nums[j]
        #                 if sum == k:
        #                     total_count += 1

        #         return total_count

        # Approach 2
        sum_count = defaultdict(int)
        sum_count[0] = 1

        count = 0
        tsum = 0
        for i in range(0, len(nums)):
            tsum += nums[i]
            diff = tsum - k

            if diff in sum_count:
                count += sum_count[diff]

            sum_count[tsum] += 1

        return count