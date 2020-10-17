def calculate(s):
    operands, operators = [], []
    operand = ""
    string_length = len(s)

    for i in range(0, string_length):
        if s[i].isdigit():
            operand += s[i]
            if i == (string_length-1) or not s[i+1].isdigit():
                operands.append(int(operand))
                operand = ""
        elif s[i] == '*' or s[i] == '/':
            operators.append(s[i])
        elif s[i] == '+' or s[i] == '-':
            while operators and (operators[-1] == '*' or operators[-1] == '/'):
                compute(operands, operators)
            operators.append(s[i])

    while operators:
        compute(operands, operators)

    return int(operands[-1])


def compute(operands, operators):
    left, right = operands.pop(), operands.pop()
    operator = operators.pop()
    if operator == '+':
        operands.append(int(left + right))
    elif operator == '-':
        operands.append(int(left - right))
    elif operator == '*':
        operands.append(int(left * right))
    elif operator == '/':
        operands.append(int(left / right))


print(calculate(s="2+2+2+2+2+10*10+2+2+2+2+2"))



# def some(b):
#     b.pop()
#
# a = [1,2,3,4,5,6]
# print(a)
# some(b=a)
# print(a)
# some(b=a)
# print(a)


