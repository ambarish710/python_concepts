# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
#


def product_array(nums):
    nums_length = len(nums)
    total, left, right = [0]*nums_length, [0]*nums_length, [0]*nums_length

    left[0] = 1
    right[nums_length-1] = 1

    #for loop
    for i in range(1, nums_length):
        left[i] = left[i-1] * nums[i-1]

    # for loop
    #for i in reversed(range(nums_length - 1)):
    for i in range(nums_length-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    # for loop
    for i in range(0, nums_length):
        total[i] = left[i] * right[i]

    return total


if __name__ == "__main__":
    input_list = [1,2,3,4,5]
    print(product_array(nums=input_list))