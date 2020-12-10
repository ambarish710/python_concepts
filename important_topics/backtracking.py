# 46. Permutations
# Medium
#
# 4963
#
# 120
#
# Add to List
#
# Share
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.


from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Using inbuilt python permutation library
        # return permutations(nums)

        # Approach 2
        # Using recursion + backtracking methodology
        self.permutations = []
        self.INPUT_LEN = len(nums)

        def backtracking(position=0):
            # if all integers are used up
            if position == self.INPUT_LEN:
                self.permutations.append(nums[:])

            for i in range(position, self.INPUT_LEN):
                # place i-th integer first
                # in the current permutation
                nums[position], nums[i] = nums[i], nums[position]

                # use next integers to complete the permutations
                backtracking(position + 1)

                # backtrack
                nums[position], nums[i] = nums[i], nums[position]

        backtracking()

        return self.permutations
