# Continuous Subarray Sum
#
# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.
#
# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
#
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        output = False

        if nums == []:
            return output

        # Logic
        total_dict = defaultdict(int)
        total_dict[0] = -1

        tsum = 0

        for i in range(0, len(nums)):
            tsum += nums[i]

            if k != 0:
                tsum = tsum % k

            if tsum in total_dict:
                if ((i - total_dict[tsum]) > 1):
                    return True
            else:
                total_dict[tsum] = i

        return output
