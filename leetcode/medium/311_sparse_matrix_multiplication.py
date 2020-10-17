# 311. Sparse Matrix Multiplication
# Medium
#
# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
# Input:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
# Output:
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
#
#
# Constraints:
#
# 1 <= A.length, B.length <= 100
# 1 <= A[i].length, B[i].length <= 100
# -100 <= A[i][j], B[i][j] <= 100



def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if len(A) == 0 or len(B) == 0:
        return [[]]

    a, c, b = len(A), len(B), len(B[0])
    AB = [[0 for _ in range(b)] for _ in range(a)]

    for i in range(a):
        for j in range(c):
            if A[i][j] != 0:
                for k in range(b):
                    if B[j][k] != 0:
                        AB[i][k] += A[i][j] * B[j][k]

    return AB



def matrix_multiplication(A,B):
    if len(A) == 0 or len(B) == 0:
        return [[]]

    result = []

    for i,row in enumerate(A):
        temp_row = []
        for j in range(len(B[0])):
            if A[i][j] != 0:
                total = 0
                for k in range(len(B)):
                    if B[k][j] != 0:
                        total += A[i][k] * B[k][j]
                temp_row.append(total)
            else:
                temp_row.append(0)
        result.append(temp_row)

    return result
