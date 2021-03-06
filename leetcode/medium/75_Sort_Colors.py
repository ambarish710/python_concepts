# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Follow up:
#
# Could you solve this problem without using the library's sort function?
# Could you come up with a one-pass algorithm using only O(1) constant space?
#
#
# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Example 3:
#
# Input: nums = [0]
# Output: [0]
# Example 4:
#
# Input: nums = [1]
# Output: [1]
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.




# Logic
# Approach 1
# Bubble sort is inplace sorting algorithm
# It is slow but in place

# Approach 2
# Dijkstra's dutch flag problem
# Algorithm
    # Initialise the rightmost boundary of zeros : p0 = 0. During the algorithm execution nums[idx < p0] = 0.
    # Initialise the leftmost boundary of twos : p2 = n - 1. During the algorithm execution nums[idx > p2] = 2.
    # Initialise the index of current element to consider : curr = 0.
    # While curr <= p2 :
    # If nums[curr] = 0 : swap currth and p0th elements and move both pointers to the right.
    # If nums[curr] = 2 : swap currth and p2th elements. Move pointer p2 to the left.
    # If nums[curr] = 1 : move pointer curr to the right.




class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums


        # Approach 2
        """
            Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1