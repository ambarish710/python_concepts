




def minRemoveToMakeValid(s):
    print(s)
    stack = []
    total = 0
    i = 0

    while i < len(s):
        print(i, stack, total)
        if s[i] == "(":
            total += 1
            stack.append(i)
        elif s[i] == ")":
            if total > 0:
                total -= 1
                stack.pop()
            else:
                print("hello: {}".format(i))
                print(s, len(s))
                s = s[:i] + s[i + 1:]
                print(s)
                i -= 1
        else:
            pass
        i += 1

    if stack == [] and total == 0:
        return s
    else:
        count = 1
        for i, position in enumerate(stack):
            if i == 0:
                s = s[:position] + s[position + 1:]
            else:
                s = s[:position-count] + s[position-count + 1:]
                count+=1

    print(total, stack, s)
    return s


if __name__ == "__main__":
    #input_string = "lee(t(c)o)de)"
    input_string = "))(("
    minRemoveToMakeValid(s = input_string)
