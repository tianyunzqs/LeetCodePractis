# -*- coding: utf-8 -*-
# @Time        : 2021/5/7 10:06
# @Author      : tianyunzqs
# @Description :

from typing import List


class Solution:
    def maxProfit_121(self, prices: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
        给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
        你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
        返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0

        *****解题思路******
        假设当前在第 i 天，令 minPrice 表示前 i-1 天的最低价格；令 maxProfit 表示前 i-1 天的最大收益。
        那么考虑第 i 天的收益时，存在两种情况：
            1.在第 i 天卖出。很显然，想要获得最大收益，应该在前 i-1 天中价格最低的时候买入，即此时的收益为：prices[i] - minPrice。
                （可能会出现负数，但是没关系）
            2.不在第 i 天卖出。那么第 i 天的最大收益就等于前 i -1 天中的最大收益
        状态转移方程为
            第 i 天最大收益 = max( 在第 i 天卖出的所得收益 , 前 i-1 天的最大收益)
        :param prices:
        :return:
        """
        if not prices:
            return 0
        minPirce = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            maxProfit = max(maxProfit, price - minPirce)
            minPirce = min(minPirce, price)
        return maxProfit

    def maxProfit_122(self, prices: List[int]) -> int:
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
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit_122(prices))
