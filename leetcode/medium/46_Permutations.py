# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]



# Logic
# Approach 1
# Using inbuilt python permutation library
    # return permutations(nums)


# Approach 2
# Using recursion and backtracking
# Have a variable where you can store all the permutations
# Store the input len in a variable
# Just understand we are just replacing two integers at a time
# We just need to change the position of the integers to replace
    # Pick a position and replace it with all
# Start from position 0 till position == len(nums)
# If position == len(nums),
    # Append nums (deep copy) to variable where you can store all the permutations
# Iterate using a for loop, replace all ints with that position and calling self recursively
# Return that variable

from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Approach 1
        # Using inbuilt python permutation library
        return permutations(nums)

        # Approach 2
        # Using recursion + backtracking methodology
        self.permutations = []
        self.INPUT_LEN = len(nums)

        def backtracking(position=0):
            # if all integers are used up
            if position == self.INPUT_LEN:
                self.permutations.append(nums[:])                       # --> VERY IMPORTANT (DEEP COPY)

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
