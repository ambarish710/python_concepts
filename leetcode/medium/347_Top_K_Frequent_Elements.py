# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.

# Logic
# Count the element occurence in a count dict
# Sort the dict in descending order
# Return k most frequent elements by iterating over dict
# [Just make sure sorted() function over dict returns a tuple list]


from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return nums

        num_count_dict = defaultdict(int)

        for num in nums:
            num_count_dict[num] += 1

        def my_sort_func(x):
            return -x[1]

        sorted_num_count_dict = sorted(num_count_dict.items(), key=my_sort_func)

        return [sorted_num_count_dict[i][0] for i in range(k)]
