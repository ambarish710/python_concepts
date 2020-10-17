def isValid(s):
    stack = []
    open_braces = ["{", "(", "["]
    close_braces = ["}", ")", "]"]

    if s:
        for x in s:
            if x in open_braces:
                stack.append(x)
            elif x in close_braces:
                if stack != []:
                    if x == "}" and stack[-1] == "{":
                        stack.pop()

                    elif x == ")" and stack[-1] == "(":
                        stack.pop()

                    elif x == "]" and stack[-1] == "[":
                        stack.pop()

                    else:
                        return False
                else:
                    return False

        if stack == []:
            return True
        else:
            return False

    else:
        return True

# input_string = "()"
# input_string = "()[]{}"
# input_string = "(]"
# input_string = "([)]"
input_string = "{[]}"
print(isValid(s=input_string))
