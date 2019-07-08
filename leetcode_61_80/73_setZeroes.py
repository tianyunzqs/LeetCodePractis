# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 18:43
# @Author      : tianyunzqs
# @Description ：

"""
73. Set Matrix Zeroes
Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


def setZeroes1(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    O(mn) space
    通过一个数组存放每个零元素的行与列，
    然后遍历该数组，将数组中的行与列分别置0
    """

    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    idx_matrix = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                idx_matrix.append((i, j))

    for i, j in idx_matrix:
        for k in range(n):
            matrix[i][k] = 0
        for k in range(m):
            matrix[k][j] = 0


def setZeroes2(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    O(m + n) space
    定义两个数组，其中一个数组存放所有零元素所在的行，
    另一个数组存放所有零元素所在的列
    然后遍历存放行和列的数组，将数组中的行与列分别置0
    """
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    idx_row, idx_col = [], []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if i not in idx_row:
                    idx_row.append(i)
                if j not in idx_col:
                    idx_col.append(j)

    for i in idx_row:
        for k in range(n):
            matrix[i][k] = 0
    for j in idx_col:
        for k in range(m):
            matrix[k][j] = 0


if __name__ == '__main__':
    matrix = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    # matrix = [[]]
    setZeroes1(matrix)
    for r in matrix:
        print(r)
