# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
# Example 1:
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
# Constraints:
#
# Methods pop, top and getMin operations will always be called on non-empty stacks.



# Logic
# What we are trying to do here is that
    # Instead of adding just one value to the stack in the form of tuple, we will add to
        # First value will be the actual value
        # Second value will be the min between first and the last pushed on stack
# The reason for doing this is the following
    # Recall that with a Stack, we only ever add (push) and remove (pop) numbers from
    # the top. Therefore, an important invariant of a Stack is that when a new number,
    # which we'll call x, is placed on a Stack, the numbers below it will not change
    # for as long as number x remains on the Stack. Numbers could come and go above x
    # for the duration of x's presence, but never below.
# So if the stack is empty then add the same number twice in tuple
# And if its not then
    # Check the last pushed values min value
    # Is current value is less than the min value push element on stack with newer min value
    # Else not
# Other operations are straighforward then
# In the tuple (actual_value, min_value_below_this_value)



class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x,x))
            return
        min_val = self.stack[-1][1]
        self.stack.append((x, min(x, min_val)))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()