# 901. Online Stock Span
#
# Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
#
# The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
#
# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
#
#
#
# Example 1:
#
# Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation:
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.
#
# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's price.
#
#
# Note:
#
# Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# There will be at most 10000 calls to StockSpanner.next per test case.
# There will be at most 150000 calls to StockSpanner.next across all test cases.
# The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.


# Logic -- Linear Scan [Works but Time Limit Exceeded]
# Add element to list and scan till price is greater than or equal to current element price
# If so increment span by 1
# Else break

class StockSpanner:

    def __init__(self):
        self.stock_prices = []

    def next(self, price: int) -> int:
        self.stock_prices.append(price)
        if len(self.stock_prices) == 1:
            return 1
        else:
            stock_span = 0
            for i in range(len(self.stock_prices) - 1, -1, -1):
                if self.stock_prices[i] <= price:
                    stock_span += 1
                else:
                    break
            return stock_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)




# Logic 2 --  Stack
# Add data to stack [last price value, span value]
# Check if last price value on the stack is less than current price value
# If yes update the stack with current value and total of 1 + span of last stack value
# Return 1 + span of last stack value
# And maintain the stack

class StockSpanner:

    def __init__(self):
        self.stock_prices_stack = []

    def next(self, price: int) -> int:
        self.stock_span = 0

        while self.stock_prices_stack and self.stock_prices_stack[-1][0] <= price:
            weight = self.stock_prices_stack.pop()[1]
            self.stock_span += weight

        self.stock_prices_stack.append([price, self.stock_span])

        return self.stock_span