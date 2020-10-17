# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
#
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

import time

def validPalindrome(s):
    if s == s[::-1]:
        return True

    for i in range(0, len(s)-1):

        s2 = s[:i] + s[i + 1:]

        if s2 == s2[::-1]:
            return True

    return False

# def validPalindrome2(s):
#     if s == s[::-1]:
#         return True
#
#     for i in range(0, len(s)-1):
#
#         s2 = s[:i] + s[i + 1:]
#
#         for j in range(0, len(s2)):
#             if s2[j] == s2[len(s2) - 1 - j]:
#                 pass
#             else:
#                 continue
#             return True
#
#     return False
#
# # def validPalindrome3(s):
# #     def is_pali_range(i, j):
# #         return all(s[k] == s[j - k + i] for k in range(i, j))
# #
# #     for i in range(len(s)/2):
# #         if s[i] != s[~i]:
# #             j = len(s) - 1 - i
# #             return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
# #     return True
#
# def validPalindrome3(s):
#         if s == s[::-1]:
#             return True
#
#         for i in range(0, len(s)):
#
#             s2 = s[:i] + s[i + 1:]
#             s2_len = len(s2)
#             count = 0
#
#             for j in range(0, int(s2_len/2) - 1):
#                 if s2[j] == s2[s2_len - 1 - j]:
#                     pass
#                 else:
#                     continue
#                 count += 1
#
#             if count > 2:
#                 if count == (s2_len / 2) - 1:
#                     return True
#
#         return False
#
#
# # def valid_palin(input_string):
# #     if input_string == input_string[::-1]:
# #         return True
# #     else:
# #         for i in range(0, len(input_string)-1):
# #             patched_string = input_string[:i] + input_string[i+1:]
# #             if patched_string == patched_string[::-1]:
# #                 return True
# #     return False
#
# def valid_palin2(input_string):
#     # logic
#     for i in range(0, len(input_string)):
#         patched_string = input_string[:i] + input_string[i+1:]
#         patched_string_half_len = int(len(patched_string)/2)
#         #print(patched_string_half_len)
#         for j in range(0, patched_string_half_len):
#             if patched_string[j] == patched_string[~j]:
#                 pass
#             else:
#                 break
#             #print(j, patched_string_half_len)
#             if j == patched_string_half_len-1:
#                 return True
#     return input_string == input_string[::-1]

def validPalindrome2(s):
    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                pass
            l += 1
            r -= 1
        return True

    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return is_palindrome(l+1, r) or is_palindrome(l, r-1)
        else:
            pass
        l += 1
        r -= 1
    return True


if __name__ == "__main__":
    some_string = "abca"*10

    t1 = time.time()
    output = validPalindrome(s=some_string)
    t2 = time.time()
    print("{} -- Time {}".format(output, t2-t1))

    # t3 = time.time()
    # output = validPalindrome2(s=some_string)
    # t4 = time.time()
    # print("{} -- Time {}".format(output, t4 - t3))
    #
    # t3 = time.time()
    # output = validPalindrome3(s=some_string)
    # t4 = time.time()
    # print("{} -- Time {}".format(output, t4 - t3))

    t5 = time.time()
    output = validPalindrome2(s=some_string)
    t6 = time.time()
    print("{} -- Time {}".format(output, t6 - t5))
