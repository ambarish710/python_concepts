# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# Follow up: Could you write an algorithm with O(log n) runtime complexity?
#
# Example 1:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
#
# Example 2:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
#
# Example 3:
# Input: nums = [], target = 0
# Output: [-1, -1]
#
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

def postion_in_an_array(nums, target):
    if nums == []:
        return [-1, -1]

    for i in range(0, len(nums)):
        if nums[i] == target:
            left_index = i
            break

    for j in range(len(nums)-1, -1, -1):
        if nums[j] == target:
            right_index = j
            break

    return [left_index, right_index]


# Approach 2
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]






# # Time Complexity is -- O(log(n))
# def find(a_list, target):
#     low = 0
#     high = len(a_list)
#
#     while low < high:
#         mid = (low+high)//2
#         if a_list[mid] == target:
#             return mid
#         elif a_list[mid] > target:
#             high = mid
#         else:
#             low = mid + 1
#
#     return None
#
#
# target = 89
# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 32, 44, 56, 72, 89]
# #INDEX    0  1  2  3  4  5  6  7   8   9   10  11  12
#
#
# ret_val = find(a_list=list_a, target=target)
# print(target, ret_val, list_a[ret_val])