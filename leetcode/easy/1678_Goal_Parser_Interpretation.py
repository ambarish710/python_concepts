# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
#
# Given the string command, return the Goal Parser's interpretation of command.
#
#
#
# Example 1:
#
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:
#
# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:
#
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
#
#
# Constraints:
#
# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.



# Logic
# Imagine you won't get output in weird order, where in it starts from ")" or something
# Iterate over command input
    # Check if char  == "("
        # If yes add all the next chars to stack till you find ")"
        # If stack empty add to output
        # Else add "o"
    # If not add char to output
# Return output



class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        output = ""
        stack = []

        while i < len(command):

            if command[i] == "(":
                i += 1

                while i < len(command):
                    if command[i] == ")":
                        if stack == []:
                            output += "o"
                        else:
                            output += "".join(stack)
                            stack = []
                        break
                    else:
                        stack.append(command[i])
                        i += 1
                else:
                    return output

            else:
                output += command[i]

            i += 1

        return output