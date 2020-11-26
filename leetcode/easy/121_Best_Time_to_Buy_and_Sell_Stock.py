# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# Logic
# Approach 1 -- Brute Force (My Approach) O(n^2)
# Have a max_profit variable and assign it to 0
# Have a for loop inside for loop and iterate over the list
# current profit == prices[j] - prices[i] if its greater than max profit
    # Update max profit
    # Else not
# Return max profit


# Approach 2 -- O(n)
# Iterate over stock price list
# Have 2 varibles
    # min_price == max int value
    # max_profit == 0
# if current price is less than min_price, update min price
# elif (which means current price > than min price), in that case check the following
    # max_profit = prices[i] - min_price
# return maX_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1 -- Brute Force (My Approach) O(n^2)
        #         max_profit = 0

        #         # if len(prices) < 2:
        #         #     return profit

        #         for i in range(len(prices)):
        #             for j in range(i+1, len(prices)):
        #                 profit = prices[j] - prices[i]
        #                 if profit > max_profit:
        #                     max_profit = profit

        #         return max_profit

        # Approach 2 -- O(n)
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit