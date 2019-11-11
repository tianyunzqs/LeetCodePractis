# -*- coding: utf-8 -*-
# @Time        : 2019/11/11 19:17
# @Author      : tianyunzqs
# @Description : 

"""
121. Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


def maxProfit(prices) -> int:
    # 单调递增栈
    in_stk = []
    # for price in prices:
    #     while in_stk and in_stk[-1] > price:
    #         in_stk.pop()
    #     in_stk.append(price)
    #
    # return in_stk

    import sys
    min_buy_price = sys.maxsize  # 最小买入价格
    max_profit = 0  # 最大收益
    for price in prices:
        # 更新最小买入价格
        min_buy_price = min(min_buy_price, price)
        # 更新收益
        max_profit = max(max_profit, price - min_buy_price)

    return max_profit


if __name__ == '__main__':
    # a = [7,6,4,3,1]
    a = [7,1,5,3,6,4]
    print(maxProfit(a))
