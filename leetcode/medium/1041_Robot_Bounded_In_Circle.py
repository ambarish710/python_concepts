# On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:
#
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
#
#
#
# Example 1:
#
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:
#
# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.
# Example 3:
#
# Input: instructions = "GL"
# Output: true
# Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
#
#
# Constraints:
#
# 1 <= instructions.length <= 100
# instructions[i] is 'G', 'L' or, 'R'.



# Logic
# Lets initialize the base positon as x-axis = 0 and y-axis = 0
# Also intialize a directions list with cordinates for
    # [up, right, down, left]
    # [(0, 1), (1, 0), (0, -1), (-1, 0)]
# And have a idx ptr which tells us which direction we are in
# Iterate over the instructions string
    # If its G add the current direction idx to x,y
    # If its L decrement idx value by 1 (coz going in left from direction list standpoint)
    # If its R increment idx value by 1 (coz going in right from direction list standpoint)
# At the end of either 1 or 4 iterrations
    # We have to check the following
        # 1st are we as the same position?
        # Or if we are in a different direction
# Thats it

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0

        for instruction in instructions:
            if instruction == "G":
                x += directions[idx % 4][0]
                y += directions[idx % 4][1]
            elif instruction == "L":
                idx -= 1
            elif instruction == "R":
                idx += 1

        return (x, y) == (0, 0) or idx % 4 != 0