# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
#
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
#
# Note:
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000


# Logic
# Create 2 arrays one even and other of off
# Iterate over the list and place all elements whose modulo == 0 in even list and other in odd list
# Return even + odd

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_array = []
        odd_array = []

        for item in A:
            if item % 2 == 0:
                even_array.append(item)
            else:
                odd_array.append(item)

        return even_array + odd_array