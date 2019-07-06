# -*- coding: utf-8 -*-
# @Time        : 2019/6/30 11:28
# @Author      : tianyunzqs
# @Description ：

"""
54. Spiral Matrix
Medium


Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


def spiralOrder(matrix):
    """
    螺旋矩阵
    定义row_min, row_max, col_min, col_max四个变量，
    按螺旋方向，分别增减以上变量，直至退出
    :param matrix:
    :return:
    """
    result = []
    if not matrix:
        return result
    row_min, row_max, col_min, col_max = 0, len(matrix)-1, 0, len(matrix[0])-1
    while row_min <= row_max and col_min <= col_max:
        # 从左到右
        flag = False  # 如果无操作，则可结束
        for j in range(col_min, col_max+1):
            result.append(matrix[row_min][j])
            flag = True
        row_min += 1
        if not flag:
            break

        # 从上到下
        flag = False
        for i in range(row_min, row_max+1):
            result.append(matrix[i][col_max])
            flag = True
        col_max -= 1
        if not flag:
            break

        # 从右到左
        flag = False
        for j in range(col_max, col_min-1, -1):
            result.append(matrix[row_max][j])
            flag = True
        row_max -= 1
        if not flag:
            break

        # 从下到上
        flag = False
        for i in range(row_max, row_min-1, -1):
            result.append(matrix[i][col_min])
            flag = True
        col_min += 1
        if not flag:
            break

    return result


"""
59. Spiral Matrix II
Medium


Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


def generateMatrix(n):
    """
    解题思路与54题类似，按螺旋方向依次填充矩阵中每个元素
    :param n:
    :return:
    """
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    row_min, row_max, col_min, col_max = 0, n - 1, 0, n - 1
    cnt = 1
    nn = n * n
    while row_min <= row_max and col_min <= col_max:
        # 从左到右
        for j in range(col_min, col_max + 1):
            matrix[row_min][j] = cnt
            cnt += 1
        row_min += 1
        if cnt > nn:
            break

        # 从上到下
        for i in range(row_min, row_max + 1):
            matrix[i][col_max] = cnt
            cnt += 1
        col_max -= 1
        if cnt > nn:
            break

        # 从右到左
        for j in range(col_max, col_min - 1, -1):
            matrix[row_max][j] = cnt
            cnt += 1
        row_max -= 1
        if cnt > nn:
            break

        # 从下到上
        for i in range(row_max, row_min - 1, -1):
            matrix[i][col_min] = cnt
            cnt += 1
        col_min += 1
        if cnt > nn:
            break

    return matrix


if __name__ == '__main__':
    matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    # matrix = [
    #   [1, 2, 3, 4],
    #   [5, 6, 7, 8],
    #   [9,10,11,12]
    # ]
    matrix = [
    ]
    # print(spiralOrder(matrix))
    print(generateMatrix(0))
