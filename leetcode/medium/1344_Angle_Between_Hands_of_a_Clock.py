# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
#
#
#
# Example 1:
#
#
#
# Input: hour = 12, minutes = 30
# Output: 165
# Example 2:
#
#
#
# Input: hour = 3, minutes = 30
# Output: 75
# Example 3:
#
#
#
# Input: hour = 3, minutes = 15
# Output: 7.5
# Example 4:
#
# Input: hour = 4, minutes = 50
# Output: 155
# Example 5:
#
# Input: hour = 12, minutes = 0
# Output: 0
#
#
# Constraints:
#
# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.


# Logic
# First find out the angle between the two hands, ignoring the diff caused bcoz hour hand will also move forward
# So just he difference between hour and minute hand can be found out using the following logic
    # Total Clock angle 360
    # So each 5 min angle = 360/12 = 30
    # So one minute angle = 30/5 = 6
    # So angle abs((hour - (minutes / 5)) * 30)
# Now caculate the difference that will be caused when hour hand moves
    # diff = minutes / 12 * 6
# Now check if diff would be added to angle or substracted from angle
    # No need to round off anywhere
    # Using the condition when can check (minutes / 5) >= hour
    # If above condition met then accurate_angle = angle - diff
    # Else accurate_angle = angle + diff
# At the end
    # Return whichever is smaller
    # accurate_angle, 360 - accurate_angle


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0

        angle = abs((hour - (minutes / 5)) * 30)
        diff = minutes / 12 * 6

        if (minutes / 5) >= hour:
            accurate_angle = angle - diff
        else:
            accurate_angle = angle + diff

        return abs(min(accurate_angle, 360 - accurate_angle))