# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# Logic
# Approach 1 Using python inbuilt library itertools.combinations
# Iterate over the list len and use the combination function
# And add it to output_list

from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output_list = []

        for i in range(len(nums) + 1):
            output_list += combinations(nums, i)

        return output_list
