# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
#
#
#
# Example 1:
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Note:
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.

# Logic
# Iterate over the list by taking squares of each number and store it in a different list
# Sort it and return the sorted list

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # B = []
        # for elem in A:
        #     B.append(elem**2)
        # B.sort()
        # return B

        return sorted(elem ** 2 for elem in A)