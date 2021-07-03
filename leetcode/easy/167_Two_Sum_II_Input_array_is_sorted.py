# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
#
#
# Constraints:
#
# 2 <= nums.length <= 3 * 104
# -1000 <= nums[i] <= 1000
# nums is sorted in increasing order.
# -1000 <= target <= 1000



# Logic
# Set low  to  0 and high to len(numbers) - 1
# iterate while low < high
# since its sorted we can use the  binary search sort off logic


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #         # Approach 1
        #         index = []

        #         for i in range(len(numbers) - 1):
        #             for j in range(i+1, len(numbers)):
        #                 total = numbers[i] + numbers[j]
        #                 if total > target:
        #                     break
        #                 elif total == target:
        #                     index.append(i+1)
        #                     index.append(j+1)

        #         return index

        # Approach 2

        low = 0
        high = len(numbers) - 1

        while low < high:
            num = numbers[low] + numbers[high]
            if num == target:
                return (low + 1, high + 1)
            elif num < target:
                low += 1
            else:
                high -= 1

        return []