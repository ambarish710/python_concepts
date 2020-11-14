# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
#
#
#
# Example 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
# Note:
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "


# Logic
# Very Interesting Approach to be honest
# Store all the alphabets only of the input string in a different list (listA)
# Now iterate over the string again and check the following, create a new output list
# If the char is an alphabet, pop a char from listA and save it in output list
# If its not an alphabet then just append the char
# Convert the list to string and return

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = [char for char in S if char.isalpha()]

        output = []

        for char in S:
            if char.isalpha():
                output.append(stack.pop())
            else:
                output.append(char)

        return "".join(output)
