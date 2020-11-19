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
# Approach 1
# Using python inbuilt library itertools.combinations
# Iterate over the list len and use the combination function
# And add it to output_list

# Approach 2
# Using recursion and backtracking
#

from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Approach 1
        output_list = []

        for i in range(len(nums) + 1):
            output_list += combinations(nums, i)

        return output_list

        # Approach 2
        self.combinations = []
        self.input_len = len(nums)

        def backtracking(k, start=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                self.combinations.append(curr[:])
            for i in range(start, self.input_len):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtracking(k, i + 1, curr)
                # backtrack
                curr.pop()

        for k in range(self.input_len + 1):
            backtracking(k=k)

        return self.combinations