# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#
#
# def decoder(ptr):
#     decoded_string = ""
#     while s[ptr] != "]":
#         decoded_string += s[ptr]
#         ptr += 1
#
#     return decoded_string, ptr
#
#
# i = 0
#
# while i < len(s):
#     output_string = ""
#     i = 0
#     while i < len(s):
#         if s[i].isdigit():
#             temp_string = ""
#             temp_num = int(s[i])
#             i += 2
#             while s[i] != "]":
#                 temp_string += s[i]
#                 i += 1
#             output_string += temp_num * temp_string
#         else:
#             output_string += s[i]
#         i += 1
#
#     return output_string
#
#
#
# stack = []
#
#
# while i < len(s)
#     if s[i].isdigit():
#         ...
#     elif s[i] == "]":
#         ...
#     elif s[i] == "[":
#         ...
#     else:


# Give a number, Write a program to output the number sequence in a list

# 0,1,1,2,3,5,8,13

# f(n) = f(n-1) + f(n-2)
# fibonacci

class fib:
    def __init__(self, n):
        self.output = [0, 1]
        self.intput = n

    def fibonacci(self):
        if self.intput == 0:
            return [0]
        if self.intput == 1:
            return self.output
        for i in range(1, self.intput):
            self.output.append(self.output[i - 1] + self.output[i])
        return self.output

    def recursion(self, n=1):
        if n == self.intput or n < 1:
            #print(n)
            if n == 0:
                return [0]
            return
        self.output.append(self.output[n - 1] + self.output[n])
        self.recursion(n=n + 1)


f_obj = fib(n=5)
# out = f_obj.fibonacci()
out = f_obj.recursion()
print(f_obj.output)
print(out)