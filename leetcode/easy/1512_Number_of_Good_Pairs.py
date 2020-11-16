# Given an array of integers nums.
#
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#
# Return the number of good pairs.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 0
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


# Logic
# Initialize total = 0
# Iterate over nums
    # Iterate over nums starting from current char + 1 (so that i < j is already satisfied)
# If orig_num == temp_num increment total
# Return total


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        for i, orig_num in enumerate(nums):
            for temp_num in nums[i+1:]:
                if orig_num == temp_num:
                    total += 1
        return total