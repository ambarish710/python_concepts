
# Write a python code to check if brackets are balanced in a given string
from collections import deque

class ParanthesisBalanceValidator:
    def __init__(self):
        self.comprehensive = ["[", "{", "(", "]", "}", ")"]
        self.start = ["[", "{", "("]
        self.close = ["]", "}", ")"]

    def validate(self, input_string):
        self.stack = deque()
        if not input_string:
            print("Error: Given input string is None")
        elif all(char not in self.comprehensive for char in input_string):
            print("Success: Paranthesis of given input {} are balanced!".format(input_string))
            return
        else:
            for character in input_string:
                if character in self.start:
                    self.stack.append(character)
                elif character in self.close:
                    # Check for [] paranthesis
                    if character == "]" and str(self.stack[-1]) == "[":
                        self.stack.pop()

                    # Check for {} paranthesis
                    elif character == "}" and str(self.stack[-1]) == "{":
                        self.stack.pop()

                    # Check for () paranthesis
                    elif character == ")" and str(self.stack[-1]) == "(":
                        self.stack.pop()

                    else:
                        print("Error: Paranthesis of given input {} are not balanced!".format(input_string))
                else:
                    pass
        print("Success: Paranthesis of given input {} are balanced!".format(input_string))

if __name__ == "__main__":
    pbv_obj = ParanthesisBalanceValidator()
    pbv_obj.validate("{Ambarish}")
    pbv_obj.validate("{[(Ambarish)]}")
    pbv_obj.validate("{[(Chaitali})]}")
    pbv_obj.validate("{}")
    pbv_obj.validate("[]")
    pbv_obj.validate("()")
    pbv_obj.validate("({(){}})")
