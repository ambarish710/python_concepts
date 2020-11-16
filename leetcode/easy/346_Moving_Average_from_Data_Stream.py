# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Example:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3



# Logic
# Create a self.nums list and a self.sliding_window_size = size
# Calculate current window size
# Find out the start and end of that window
# Make sure start and end are within the list len bounds
# Calulate the total of the elements in that window and divide it by the window len
# Return the average



class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sliding_window_size = size
        self.nums = []

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.curr_window = len(self.nums) - self.sliding_window_size

        start = 0 if (self.curr_window) < 0 else self.curr_window
        end = start + self.sliding_window_size

        if end > len(self.nums):
            self.total = 0
            for num in self.nums:
                self.total += num
            return self.total / len(self.nums)
        else:
            self.total = 0
            for num in self.nums[start:end]:
                self.total += num
            return self.total / len(self.nums[start:end])

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
