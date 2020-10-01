# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a, b):
        return '{0:b}'.format( int(a, 2) + int(b, 2) )

    # Not Working
    # def addBinary2(self, a, b):
    #     carry = 0
    #     total = []
    #     n = max(len(a), len(b))
    #     a, b = a.zfill(n), b.zfill(n)
    #
    #     for i in range(n-1, -1, -1):
    #         add = int(a[i]) + int(b[i]) + carry
    #
    #         if add > 1:
    #             total += "1"
    #             carry = 1
    #         elif add == 1:
    #             total += "1"
    #             carry = 0
    #         else:
    #             total += "0"
    #             carry = 0
    #
    #     if carry == 1:
    #         total += "1"
    #
    #     return total

if __name__ == "__main__":
    s_obj = Solution()
    a = "111"
    b = "10"
    #total = s_obj.addBinary("111", "10")
    #print("{}+{}={}".format(int("111", 2), int("101", 2), int(total, 2)))
    total = s_obj.addBinary2(a, b)
    print("{}+{}={}".format(int(a, 2), int(b, 2), int(total, 2)))
