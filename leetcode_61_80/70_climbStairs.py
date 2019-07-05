# -*- coding: utf-8 -*-
# @Time        : 2019/7/3 10:40
# @Author      : tianyunzqs
# @Description : 

"""
70. Climbing Stairs
Easy


You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


def climbStairs(n: int) -> int:
    # # solution1
    # dp = [1 for _ in range(n+1)]
    # dp[0] = dp[1] = 1
    # for i in range(2, n+1):
    #     dp[i] = dp[i-2] + dp[i-1]
    #
    # return dp[-1]

    # solution2
    if n < 2:
        return 1
    else:
        return climbStairs(n-2) + climbStairs(n-1)


print(climbStairs(3))
