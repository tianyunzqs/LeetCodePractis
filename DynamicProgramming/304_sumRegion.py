# -*- coding: utf-8 -*-
# @Time        : 2020/8/27 9:38
# @Author      : tianyunzqs
# @Description : 

"""
304. Range Sum Query 2D - Immutable
Medium

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined
by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3),
which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

from typing import List


class NumMatrix0:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_region = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum_region += self.matrix[i][j]
        return sum_region


class NumMatrix:
    """
    dp[i][j]表示从(0, 0)到(i, j)矩形内元素之和
    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
    """
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.dp = []
        else:
            m, n = len(matrix), len(matrix[0])
            self.dp = [[0 for _ in range(n)] for _ in range(m)]
            self.dp[0][0] = matrix[0][0]
            for i in range(1, m):
                self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]
            for j in range(1, n):
                self.dp[0][j] = self.dp[0][j-1] + matrix[0][j]
            for i in range(1, m):
                for j in range(1, n):
                    self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp:
            return None
        if row1 <= 0 and col1 <= 0:
            return self.dp[row2][col2]
        if row1 <= 0 and col1 > 0:
            return self.dp[row2][col2] - self.dp[row2][col1 - 1]
        if row1 > 0 and col1 <= 0:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2]
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    print(NumMatrix(matrix).sumRegion(0, 1, 4, 3))
    print(NumMatrix(matrix).sumRegion(2, 1, 4, 3))
    print(NumMatrix(matrix).sumRegion(1, 1, 2, 2))
    print(NumMatrix(matrix).sumRegion(1, 2, 2, 4))
    print(NumMatrix([[]]).sumRegion(1, 2, 2, 4))
