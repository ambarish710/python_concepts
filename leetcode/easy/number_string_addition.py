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
for character in string_1:
    if character == "-":
        if number != "":
            total += float(number)
            number = ""
        number = "-"
    elif character == "+":
        if number != "":
            total += float(number)
            number = ""
    else:
        number += character

total += float(number)
print(total)
