# -*- coding: utf-8 -*-
# @Time        : 2020/8/18 22:13
# @Author      : tianyunzqs
# @Description ：

"""
264. Ugly Number II
Medium

Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:
1 is typically treated as an ugly number.
n does not exceed 1690.
"""


class Solution:
    """
    dp[i]表示第i个丑数（ugly number）
    定义三个下标指示器（t2, t3, t5），主要作用是为了排除min计算出来已经存在于dp中的数
    dp下一个数 = 所有已存在的数分别乘以2，3，5后的最小值，并且该最小值未出现在dp列表中
    如：dp[0] = 1
    dp[1] = min(dp[0]*2, dp[0]*3, dp[0]*5) = 2
    dp[2] = min(dp[1]*2, dp[0]*3, dp[0]*5) = 3（因为dp[0]*2已经考虑过了，t2指针+1）
    dp[3] = min(dp[1]*2, dp[1]*3, dp[0]*5) = 4（因为dp[0]*2和dp[1]*3已经考虑过了，t2+1, t3+1）
    dp[4] = min(dp[2]*2, dp[1]*3, dp[0]*5) = 5（因为dp[0]*2、dp[1]*3、dp[1]*2已经考虑过了，t2+1, t3+1, t2+1）
    dp[5] = min(dp[2]*2, dp[1]*3, dp[1]*5) = 6（因为dp[0]*2、dp[1]*3、dp[1]*2、dp[0]*5已经考虑过了，t2+1, t3+1, t2+1, t5+1）
    dp[6] = min(dp[3]*2, dp[2]*3, dp[1]*5) = 8（因为dp[2]*2、dp[1]*3都等于6，因此，本次t2+1，同时t3+1）
    故可不用考虑最小值在dp列表中的情形
    """
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return None
        if n == 1:
            return 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        t2, t3, t5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min([dp[t2] * 2, dp[t3] * 3, dp[t5] * 5])
            if dp[i] == dp[t2] * 2:
                t2 += 1
            if dp[i] == dp[t3] * 3:
                t3 += 1
            if dp[i] == dp[t5] * 5:
                t5 += 1
        return dp[n-1]


if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))
