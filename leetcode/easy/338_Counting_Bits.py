# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

# Logic
# Iterate using for loop till num
# Convert each int into binary string using {0:b}.format(int(1))
# Then use inbuilt python method count. To count the number of 1's
# Add it to a temp list
# Return temp list

class Solution:
    def countBits(self, num: int) -> List[int]:
        output_list = []
        for i in range(num+1):
            a = "{:b}".format(i)
            output_list.append(a.count("1"))
        return output_list