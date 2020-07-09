# -*- coding: utf-8 -*-
# @Time        : 2020/7/8 18:45
# @Author      : tianyunzqs
# @Description : 

"""
188. Best Time to Buy and Sell Stock IV
Hard

Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


class Solution:
    """
    未看懂
    """
    def maxProfit(self, k: int, prices: list) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 如果价格列表不足2个元素，则不需要交易，收益也就为0
        if n < 2:
            return 0
        # 如果运行交易次数，大于价格列表长度的一半，则只要后一个价格大于前一个价格，即可完成一次交易
        # 这里会存在卖出后立即买入的情况，此种情况跟跳过当前价格是等价的
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i > j)
        # dp[i][j]表示在第j个元素上，完成第i次交易的最大收益
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]
        for i in range(1, k + 1):
            maxval = -prices[0]
            for j in range(1, n):
                # 没看懂
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxval)
                maxval = max(maxval, dp[i - 1][j] - prices[j])
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().maxProfit(k=2, prices=[2, 4, 1]))
    print(Solution().maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
    print(Solution().maxProfit(k=5, prices=[1, 2, 3, 4, 5]))
