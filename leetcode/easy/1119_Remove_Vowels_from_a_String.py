# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
#
#
#
# Example 1:
#
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:
#
# Input: "aeiou"
# Output: ""
#
#
# Note:
#
# S consists of lowercase English letters only.
# 1 <= S.length <= 1000

# Logic
# Keep vowels in a string
# Iterate over S and check each char not in string
# And add that char to output
# And return it once done

class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = "aeiou"
        output = ""
        for s in S:
            if s not in vowels:
                output += s
        return output
