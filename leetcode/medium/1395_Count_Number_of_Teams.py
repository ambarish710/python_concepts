# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
#
# You have to form a team of 3 soldiers amongst them under the following rules:
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
#
#
#
# Example 1:
#
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
# Example 2:
#
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
# Example 3:
#
# Input: rating = [1,2,3,4]
# Output: 4
#
#
# Constraints:
#
# n == rating.length
# 1 <= n <= 200
# 1 <= rating[i] <= 10^5



# Logic
# Initialize spcl_combs or output to 0
# If len rating less than 3, return 0
# Use python in built package combinations to get all the 3 int combinations
# Else iterate over the combinations list
    # And check if you qualify for any of the given conditions
    # And if you do increment output or spcl_combs by 1
# Return output


from itertools import combinations


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        output = 0

        if len(rating) < 3:
            return output

        n = len(rating)
        comb_list = combinations(rating, 3)

        for comb in comb_list:
            if comb[0] < comb[1] < comb[2]:
                output += 1
            elif comb[0] > comb[1] > comb[2]:
                output += 1
            elif 0 <= comb[0] < comb[1] < comb[2] < n:
                output += 1

        return output