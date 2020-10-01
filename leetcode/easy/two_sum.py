# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]


class Solution:
    # TC -- O(n^2)
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]

    # TC -- O(n)
    def twosum2(self, nums, target):
        self.num_dict ={}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in self.num_dict.keys():
                return[i, self.num_dict[diff]]
            else:
                self.num_dict[nums[i]] = i


if __name__ == "__main__":
    sobj = Solution()
    print(sobj.twosum2([1,2,3,4,5], 8))
