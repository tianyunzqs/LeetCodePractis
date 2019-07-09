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


def setZeroes3(matrix):
    '''
    Idea:
    Use a var to store the line # of which has the first 0.
    Use that line as a mask line. update the all items in that line to 1.
    When we meet a 0, update the mask line's same index item to 0,
        and then update the items in current line to 0.
    Make a new loop which uses the mask line to do 'and' operation with each line.
    At the end, change the the mask line to all 0.
    '''

    mask = -1
    high = len(matrix)
    width = len(matrix[0])
    for r in range(high):
        clear = False
        for c in range(width):
            if matrix[r][c] == 0:
                if mask == -1:  # Meet the first 0
                    mask = r  # Get the mask line number
                    for i in range(width):  # The 0 in the mask line will keep 0, change other items to 1
                        matrix[mask][i] = 1 if matrix[mask][i] != 0 else 0
                    break  # We don't want to clear the mask line
                else:  # Meet any other line which has 0
                    clear = True  # Will clear the line to all 0
                matrix[mask][c] = 0  # Update the mask.
        if clear:
            matrix[r] = [0] * width  # Clear the current line which has 0
    if mask == -1:  # In case of no 0 at all
        return
    for r in range(high):
        for c in range(width):  # Use mask to do 'and' with each line
            matrix[r][c] = matrix[mask][c] and matrix[r][c]
    matrix[mask] = [0] * width  # Clear the mask line


def setZeroes4(matrix):
    # First row has zero?
    m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
    # Use first row/column as marker, scan the matrix
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0
    # Set the zeros
    for i in range(1, m):
        for j in range(n - 1, -1, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # Set the zeros for the first row
    if firstRowHasZero:
        matrix[0] = [0] * n


if __name__ == '__main__':
    matrix = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    # matrix = [[]]
    setZeroes4(matrix)
    for r in matrix:
        print(r)
