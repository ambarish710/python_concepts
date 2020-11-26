# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]


# Logic
# Approach 1 --
# TC -- O(n)
# SC -- O(n)
# Count the number of iterations for a num
# If count > 2 add it to duplicates set
# Return it


# Approach 2
# TC -- O(n)
# SC -- O(1)
# Update the nums list inplace
# You have to understand that the total at the given index can never be twice that of the maximum
# Coz there is a constraint about the nums in the list, that they are less than the len(list)
# So we are using maths to solve the problem
# Lets update the value on this index,
    # nums[nums[i] % n] by = nums[nums[i] % n] + n
# So only in the case of duplicates the value on that place will be more than 2(len(list)
# Now iterate the updated list and whereever you find num > 2n
    # Append the index position to the ret_list (here the index position will act as the num -- VIMP)
# Return ret_list


from collections import defaultdict


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Approach 1
        nums_count = defaultdict(int)

        duplicates = set()

        for num in nums:
            nums_count[num] += 1
            if nums_count[num] > 1:
                duplicates.add(num)

        return duplicates



        # Approach 2
        n = len(nums)

        if n == 0:
            return
        res = []

        for i in range(n):
            nums[nums[i] % n] = nums[nums[i] % n] + n

        if nums[0] > n * 2:
            # Covering corner case
            # since the array includes n , for n it is stored in 0th index
            res.append(n)

        for i in range(0, n):
            if nums[i] > n * 2:
                res.append(i)

        return res