# -*- coding: utf-8 -*-
# @Time        : 2021/5/7 9:31
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
122. 买卖股票的最佳时机 II
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


示例 1:
输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: prices = [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: prices = [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


提示：
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""

from typing import List


class Solution:
    def maxProfit2(self, prices: List[int]):
        res = []
        for price in prices:
            while res and res[-1] > price:
                res.pop()
            res.append(price)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
        给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

        *****解题思路******
        考虑到对于任意一天，要么持有股票（定义该状态为 hold），要么不持有股票（定义该状态为 sold）。
        假设第 i 天为 hold 状态：
            case 1：可能前一天是 hold 状态，即在第 i-1 天持有股票，在第 i 天时继续持有，啥也不干（我们定义“啥也不干”这一动作为 rest）；
            case 2：可能前一天是 sold 状态，即在第 i-1天本来是不持有股票的，但是在第 i 天买入了一支新股，因此第 i 天变成了 hold 状态。

        假设第 i 天为 sold 状态：
            case 1：可能前一天是 hold 状态，即在第 i-1 天持有股票，但是在第 i 天时抛售了，于是变成了 sold 状态；
            case 2：可能前一天是 sold 状态，即在第 i-1天不持有股票的，在第 i 天继续啥也不干。
        基于上面的分析，可以画出如下状态机转换示意图（原创图，ppt画的）：

        上面是理论分析，落实到代码层面，我们定义变量hold和sold表示第 i 天结束后所拥有的收益。
        很显然，最后的结果保存在sold中，即卖完手中的股票总比还持有股票要多套现一点钱的。根据状态机，我们可以写出如下状态状态转移方程：

        假设当前是第 i 天
            hold = max(prev_hold, prev_sold - prices[i]);
            sold = max(prev_sold, prev_hold + prices[i]);
        :param prices:
        :return:
        """
        if not prices:
            return 0
        sold, hold = 0, -prices[0]  # 第一天需要花钱买入，因此受益为-prices[0]
        for price in prices:
            prev_sold = sold
            prev_hold = hold
            hold = max(prev_hold, prev_sold - price)
            sold = max(prev_sold, prev_hold + price)
        return sold


if __name__ == '__main__':
    nums = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit2(nums))
