# Only reason for using deque instead of normal list is because
# list == dynamic arrays and if the size crosses the default limit
# and you try to add more elements then entire array needs to be copied
# to the next location (with size of current size*2 and copy all elements)
# and then add required element. This is very mem and cpu
# not intensive. Hence use deque it handles it properly using doubly LL.
from collections import deque

class StackClass:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def peek(self):
        print(self.stack)

    def stack_size(self):
        print(len(self.stack))


if __name__ == "__main__":
    sc_obj = StackClass()
    sc_obj.push(5)
    sc_obj.push(10)
    sc_obj.push(15)
    sc_obj.peek()
    sc_obj.stack_size()
    sc_obj.pop()
    sc_obj.peek()
    sc_obj.stack_size()
