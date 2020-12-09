# Given an integer array nums, design an algorithm to randomly shuffle the array.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
#
#
# Example 1:
#
# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
#
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# -106 <= nums[i] <= 106
# All the elements of nums are unique.
# At most 5 * 104 calls will be made to reset and shuffle.



# Logic
# Create two list
    # one given
    # Deep Copy of the same list  (which will act as the original list)

# Reset
    # Override self.nums with original list
    # return nums

# Shuffle
    # Use python random function of list selection
    # Copy the nums list in a temp list
    # Iterate in while loop till temp list is emtpy
        # Select an element randomly from temp list
        # Add it to nums list
        # Delete it from temp list
    # Return the shuffled list


import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = self.nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        temp = self.nums[:]
        self.nums.clear()
        while temp:
            val = random.choice(temp)
            self.nums.append(val)
            temp.remove(val)
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()