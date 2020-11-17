# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2


# Logic
# Count the number of occurrences of ints in nums
# Then find the int which has occurred the most and return it

from collections import Counter, defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 1
        # nums_counter = Counter(nums)
        # return nums_counter.most_common(1)[0][0]

        # Approach 2
        nums_counter = defaultdict(int)
        for num in nums:
            nums_counter[num] += 1
        print(nums_counter)
        max_element, max_occurence = 0, len(nums) / 2

        for key, val in nums_counter.items():
            if val > max_occurence:
                max_element = key
                break

        return max_element