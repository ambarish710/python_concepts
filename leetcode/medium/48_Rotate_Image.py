# 48. Rotate Image
# Medium

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:
#
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# Example 3:
#
# Input: matrix = [[1]]
# Output: [[1]]
# Example 4:
#
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
#
#
# Constraints:
#
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


# Logic
# The obvious idea would be to transpose the matrix first and then reverse each row.
# This simple approach already demonstrates the best possible time complexity O(N^2).
# Matrix Transpose -- We can transpose a matrix by switching its rows with its columns.
# Reversing each list of the transposed list, will give you the rotated matrix you require

# INPUT                 # OUTPUT EXPECTED
# 00 01 02              # 20 10 00
# 10 11 12              # 21 11 01
# 20 21 22              # 22 12 02

# INPUT                 # Transpose         # Reverse of Transposed Cell
# 00 01 02              # 00 10 20          # 20 10 00
# 10 11 12              # 01 11 21          # 21 11 01
# 20 21 22              # 02 12 22          # 22 12 02

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = matrix[i][::-1]

        return matrix


if __name__ == "__main__":
    s_obj = Solution()
    output = s_obj.rotate([[1,2,3],[4,5,6],[7,8,9]])
    print(output)
