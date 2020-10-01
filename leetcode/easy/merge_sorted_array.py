# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
#
# Example:
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]




class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        nums1_copy = nums1[:m]
        nums1[:] = []

        while i < m and j < n:

            if nums1_copy[i] < nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1

        if j < n:
            nums1 += nums2[j:]
        if i < m:
            nums1 += nums1_copy[i:]
