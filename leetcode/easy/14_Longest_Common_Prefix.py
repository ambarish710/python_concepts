# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.


# Logic
# Find the length of the shortest string in the list of strs
# Check if its 0 or strs is empty in that case return ""
# Create a int variable to store common value int
# Iterate over strs till min_len (so that we will check only those chars)
# Store current char in temp_char variable
# Iterate over the strs and check if astr[i] != temp_char:
    # if its not then return strs[0][:lcp]
# Else increment lcp (which means all strings have the same char at that position)
# Finally, return strs[0][:lcp]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find min length
        min_len = float("inf")
        for astr in strs:
            if len(astr) < min_len:
                min_len = len(astr)

                # Corner case check
        if min_len == 0 or strs == []:
            return ""

        # Check LCP
        lcp = 0
        for i in range(min_len):
            temp_char = strs[0][i]
            for astr in strs:
                if astr[i] != temp_char:
                    return strs[0][:lcp]
            lcp += 1
        return strs[0][:lcp]
