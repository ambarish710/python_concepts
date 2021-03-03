# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105





# Logic
# So the logic is to find the following
    # From the current point find the left most maximum and right most maximum
    # Take the minimum of them
    # Then substract current value
    # Thats water at that specific location
# Iterate over the water list from position 1 and go forward





class Solution:
    def trap(self, height: List[int]) -> int:
        rain_water = 0

        for i in range(1, len(height) - 1):
            hmin = min(max(height[:i]), max(height[i + 1:]))
            if hmin - height[i] > 0:
                rain_water += hmin - height[i]

        return rain_water
