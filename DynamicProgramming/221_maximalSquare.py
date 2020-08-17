# -*- coding: utf-8 -*-
# @Time        : 2020/8/17 21:43
# @Author      : tianyunzqs
# @Description ：

"""
221. Maximal Square
Medium

Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

Example:
Input:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution:
    """
    dp[i][j]表示以(i,j)为终点组成的方形的最大边长
    当i=0 或者 j=0 时，dp[i][j] = matrix[i][j]，因为此时以(i,j)为终点组成的方形只有(i,j)一个点
    当matrix[i][j] == 0 时，此时以(i,j)为终点组成的方形为0
    当i>0 and j>0 and matrix[i][j] == 1 时，
    此时以(i,j)为终点组成的方形边长由其左边、上边、左上角三者中最小值决定，由于(i,j)位置为1，所以需要加1
    边长取最大值
    """
    def maximalSquare(self, matrix: list) -> int:
        sz = 0
        try:
            m, n = len(matrix), len(matrix[0])
        except IndexError:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        matrix = [list(map(int, row)) for row in matrix]
        for i in range(m):
            for j in range(n):
                if not i or not j or matrix[i][j] == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                sz = max(dp[i][j], sz)
        return sz * sz


if __name__ == '__main__':
    a = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    print(Solution().maximalSquare(a))
