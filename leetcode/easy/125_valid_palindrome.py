# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
# Example 2:
# Input: "race a car"
# Output: false


def isPalindrome(input_string):
    if input_string == None:
        return True

    formated_string = []
    for alphabet in input_string.lower():
        ascii = ord(alphabet)
        if (ascii >= 97 and ascii <= 122) or (ascii >= 48 and ascii <= 57):
            formated_string.append(alphabet)

    print(formated_string)
    return formated_string == formated_string[::-1]


if __name__ == "__main__":
    print(isPalindrome(input_string="Marge, let's \"[went].\" I await {news} telegram."))
