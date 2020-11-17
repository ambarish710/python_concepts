# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one duplicate number in nums, return this duplicate number.
#
# Follow-ups:
#
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem without modifying the array nums?
# Can you solve the problem using only constant, O(1) extra space?
# Can you solve the problem with runtime complexity less than O(n2)?
#
#
# Example 1:
#
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
#
# Input: nums = [1,1]
# Output: 1
# Example 4:
#
# Input: nums = [1,1,2]
# Output: 1
#
#
# Constraints:
#
# 2 <= n <= 3 * 104
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.




# Logic
# Approach 1
# Count the num char occurences in dict O(n)
# Iterate over the list and check if num dict O(n) + O(1)
# Final TC --> O(n) + O(n) + O(1) = O(n)
# But SC --> O(n) worst case scenario

# Approach 2 (Better bcoz of less SC and that was the req of this problem)
# Sort the num O(nlogn)
# Iterate over list O(n)
# Check if num at position i equal to num at postion i + 1
# Return that num
# Final TC --> O(nlogn) + O(n) = O(nlogn)
# But SC --> O(1) worst case scenario

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # count_dict = {}
        # for num in nums:
        #     if num not in count_dict:
        #         count_dict[num] = 1
        #     else:
        #         return num

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]