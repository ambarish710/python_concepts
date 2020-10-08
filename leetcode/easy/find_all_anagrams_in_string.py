# Find All Anagrams in a String
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".




from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram_list = []

        plength = len(p)
        slength = len(s)

        if len(p) > len(s):
            return anagram_list

        i = 0
        j = plength

        # Requirement for approach 3
        # temp_p = sorted(p)

        # Requirement for approach 4
        p_count = Counter(p)

        while (i + j) <= slength:
            # Approach 1 -- (Timeout)
            # temp_p = p
            # temp_s = s[i:i+j]
            # if Counter(temp_p) == Counter(temp_s):
            #     anagram_list.append(i)

            # Approach 2 -- (Doesn't Work)
            # if all(s[k] in p for k in range(i, i+j)):
            #     anagram_list.append(i)

            # Approach 3 -- Works (7% better than most)
            # if temp_p == sorted(s[i:i+j]):
            #     anagram_list.append(i)

            # Approach 4 -- 12.54% better than others
            temp_s_count = Counter(s[i:i + j])
            if temp_s_count == p_count:
                anagram_list.append(i)

            i += 1

        return anagram_list