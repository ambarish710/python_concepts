# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
#
# Can you solve it in O(N) time and O(1) space?



# Logic
# Create 2 lists string1 and string2
# Iterate over S and if char is alphabet add it to string1 or if its # delete last element from string1
# Iterate over T and if char is alphabet add it to string2 or if its # delete last element from string2
# Check if string 1 == string 2 if yes return True else False



class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        string1 = []
        string2 = []

        for char in S:
            if char.isalpha():
                string1.append(char)
            elif char == "#" and len(string1) > 0:
                del string1[-1]

        for char in T:
            if char.isalpha():
                string2.append(char)
            elif char == "#" and len(string2) > 0:
                del string2[-1]

        return "".join(string1) == "".join(string2)