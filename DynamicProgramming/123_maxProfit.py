# -*- coding: utf-8 -*-
# @Time        : 2020/5/16 22:00
# @Author      : tianyunzqs
# @Description :

"""
123. Best Time to Buy and Sell Stock III
Hard

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    """
    Maximum two profits equals to :
        max(second_sell - second_buy + first_sell - first_buy)
        max(second_sell - (second_buy - first_sell + first_buy))
        max(second_sell - (second_buy - (first_sell - first_buy)))

    Bring in the variables in the code:
        max(second_sell - (second_buy - (first_profit))
        max(second_sell - second_buy_first_profit)
    """
    def maxProfit(self, prices: list) -> int:
        first_buy, first_profit, second_buy_first_profit, max_profit = float('inf'), 0, float('inf'), 0
        for price in prices:
            first_buy = min(first_buy, price)
            first_profit = max(first_profit, price - first_buy)
            second_buy_first_profit = min(second_buy_first_profit, price - first_profit)
            max_profit = max(max_profit, price - second_buy_first_profit)
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
