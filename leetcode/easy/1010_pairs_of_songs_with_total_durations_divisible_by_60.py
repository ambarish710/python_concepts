# In a list of songs, the i-th song has a duration of time[i] seconds.
#
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
#
#
#
# Example 1:
#
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# Example 2:
#
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.
#
#
# Note:
#
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500


# Logic comes from here
# Modulo concepts
# 		100 % 60 == 40
# 		-100 % 60 == 20
# 		-30 % 60 == 30
# - always gives you what you require
# Create a default dict of what you require
# And increase it by 1 if thats what it requires to be divisible by 60
# And add those values
# Boom you're done

from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count_dict = defaultdict(int)
        total = 0
        for t in time:
            total += count_dict[-t % 60]
            count_dict[t % 60] += 1
        return total


# Not accepted O(n^2) logic
# def numPairsDivisibleBy60(self, time: List[int]) -> int:
#     total_pairs = 0
#
#     if not time:
#         return total_pairs
#
#     for i in range(0, len(time)):
#         for j in range(i+1, len(time)):
#             if ((time[i] + time[j])%60) == 0:
#                 total_pairs += 1
#
#     return total_pairs
