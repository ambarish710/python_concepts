# 398. Random Pick Index
# Medium
# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
#
# Example:
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);

# Create a defaultdict of list
# Iterate over nums list and add num (key) and its index as value
# Find the index list for target and select randonly and return

import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_index = defaultdict(list)
        for i, num in enumerate(nums):
            self.nums_index[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.nums_index[target])
