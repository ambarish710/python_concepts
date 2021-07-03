# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
#
# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
#
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
#
#
#
# Example 1:
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
# Example 2:
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
# Example 3:
#
# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
#
#
# Constraints:
#
# p1.length == p2.length == p3.length == p4.length == 2
# -104 <= xi, yi <= 104


# Logic
# There are just 6 line possibilities
# Calculate all six, then sort them
# First 4 will be sides and last two will be diagonals
# Check  if first 4 equal and > 0 (len of side)
# Check if 5,6 are equal and twice the size  of any  of the first 4


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def side_len(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        sides = [side_len(p1, p2), side_len(p1, p3), side_len(p1, p4),
                 side_len(p2, p3), side_len(p2, p4), side_len(p3, p4)]

        sides.sort()

        if sides[0] == sides[1] == sides[2] == sides[3] and sides[0] > 0:
            if sides[4] == sides[5] and (sides[0] * 2) == sides[4]:
                return True

        return False