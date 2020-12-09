# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?



# Logic
# Count the element occurence for both nums1 and nums2
# Compare which one is smaller in length
# Iterate over the smaller dict
    # Check if the element exits in other dict
    # And if it does get the common occurences
        # Which will be the min between that element and other dicts same element occurences
    # Append the number to the ret list that many times
# Return ret list



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []

        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)

        if len(nums1_count) < len(nums2_count):
            for key, value in nums1_count.items():
                if key in nums2_count:
                    ret += [key] * min(value, nums2_count[key])
        else:
            for key, value in nums2_count.items():
                if key in nums1_count:
                    ret += [key] * min(value, nums1_count[key])
        return ret