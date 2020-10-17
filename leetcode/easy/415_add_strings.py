import time

class Solution:
    def addStrings(self, num1, num2):
        num1_int = self.convert_string_to_integer(num1)
        num2_int = self.convert_string_to_integer(num2)
        total = num1_int + num2_int
        return str(total)

    def convert_string_to_integer(self, number_string):
        integer_value = 0
        string_len = len(number_string)
        number_dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                       "6": 6, "7": 7, "8": 8, "9": 9}

        for i in range(0, len(number_string)):
            #print(number_dict[number_string[i]])
            integer_value += (number_dict[number_string[i]] * (10 ** ((string_len - 1) - i)))

        return integer_value

    def addStrings2(self, num1, num2):
        res = []

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])


if __name__ == "__main__":
    s_obj = Solution()

    t1 = time.time()
    total = s_obj.addStrings(num1="121555", num2="124333")
    t2 = time.time()
    print(total, t2-t1)

    t3 = time.time()
    total = s_obj.addStrings2(num1="121555", num2="124333")
    t4 = time.time()
    print(total, t4-t3)
