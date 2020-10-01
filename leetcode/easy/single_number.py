# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


class Solution:
    def singleNumber(self, nums):
        self.count = []
        for num in nums:
            if num not in self.count:
                self.count.append(num)
            else:
                self.count.remove(num)
        return self.count[0]

    def singleNumber2(self, nums):
        out = 0
        for num in nums:
            out = out ^ num
        return out

if __name__ == "__main__":
    s_obj = Solution()
    print(s_obj.singleNumber2([2,2,1]))