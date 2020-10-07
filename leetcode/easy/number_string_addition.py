# string_1 = "-12.3-40+50-60"
# total = 0
# number = ""
#
# for character in string_1:
#     if character == "+":
#         if number != "":
#             total += float(number)
#         number = "+"
#     elif character == "-":
#         if number != "":
#              total += float(number)
#         number = "-"
#     else:
#         number += character
#
# total += float(number)
# print(total)



















string_1 = "-12.3-40+50-60"

total = 0
number = ""

for i in range(0, len(string_1)):
    if string_1[i] == "+":
        if number != "":
            total += float(number)
        number = ""
    elif string_1[i] == "-":
        if number != "":
            total += float(number)
        number = "-"
    else:
        number += string_1[i]

# Pass
#print(number)
total += float(number)
print(total)





#
# total = 0
# number = ""
# for character in string_1:
#     if character == "-":
#         if number != "":
#             total += float(number)
#             number = ""
#         number = "-"
#     elif character == "+":
#         if number != "":
#             total += float(number)
#             number = ""
#     else:
#         number += character
#
# total += float(number)
# print(total)
