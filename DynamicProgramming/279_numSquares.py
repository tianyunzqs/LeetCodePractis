# -*- coding: utf-8 -*-
# @Time        : 2020/8/19 21:30
# @Author      : tianyunzqs
# @Description ：

"""
279. Perfect Squares
Medium

Given a positive integer n,
find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

import sys


class Solution:
    """
    cnt[i]表示累计和等于i的最少平方数个数
    cnt[0] = 0
    cnt[1] = 1
    如果len(cnt) > n，则表示计算结束
    第二个while循环用于计算cnt[i]
    """
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        cnt = [0]
        while len(cnt) <= n:
            m = len(cnt)
            cnt_tmp = sys.maxsize
            i = 1
            while i * i <= m:
                # 优先取最大的平方数
                cnt_tmp = min(cnt_tmp, cnt[m - i * i] + 1)
                i += 1
            cnt.append(cnt_tmp)
        return cnt[n]


if __name__ == '__main__':
    print(Solution().numSquares(12))
    print(Solution().numSquares(13))
