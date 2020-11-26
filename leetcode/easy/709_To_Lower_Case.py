# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#
#
#
# Example 1:
#
# Input: "Hello"
# Output: "hello"
# Example 2:
#
# Input: "here"
# Output: "here"
# Example 3:
#
# Input: "LOVELY"
# Output: "lovely"



# Logic
# Check is the current char is between "A" and "Z" (using ord)
    # If yes convert it lower char using ord and chr inbuilt methods
    # If not append the char directly to the new string
# Return lower case string



class Solution:
    def toLowerCase(self, str: str) -> str:
        lower_case_string = ""
        MIN_ORD = ord("A")
        MAX_ORD = ord("Z")

        for s in str:
            curr_char_ord = ord(s)
            if MIN_ORD <= curr_char_ord <= MAX_ORD:
                lower_case_converted_char = curr_char_ord + 32
                lower_case_string += chr(lower_case_converted_char)
            else:
                lower_case_string += s

        return lower_case_string