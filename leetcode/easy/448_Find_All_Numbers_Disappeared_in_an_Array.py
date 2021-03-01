# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]


# Logic
# Create a hashmap and store all elements and its occurences
# Now iterate over the range list
# Check is element in hashmap


from collections import defaultdict


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret_list = []
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        for i in range(1, len(nums) + 1):
            if i not in hashmap:
                ret_list.append(i)

        return ret_list

