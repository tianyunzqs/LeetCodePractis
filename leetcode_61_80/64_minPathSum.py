# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 18:26
# @Author      : tianyunzqs
# @Description ：

"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


def minPathSum(grid) -> int:
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[-1][-1]


if __name__ == '__main__':
    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    print(minPathSum(grid))
