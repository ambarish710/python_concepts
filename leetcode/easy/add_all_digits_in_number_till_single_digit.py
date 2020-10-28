# Add all digits in an integer till sum in one character
a = 5929

7

def addinst(inint):
    total = 0
    for char in str(inint):
        total += int(char)
    return total


while len(str(a)) > 1:
    a = addinst(inint=a)

print(a)