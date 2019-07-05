# -*- coding: utf-8 -*-
# @Time        : 2019/6/27 10:00
# @Author      : tianyunzqs
# @Description : 

import numpy as np


def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    a = np.array(matrix)
    b = a.transpose()
    return [list(bb[::-1]) for bb in b]


def rotate2(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    先将矩阵上下翻转，然后将所有斜对角线上的元素互换即可
    """
    N = len(matrix)
    for i in range(N // 2):
        for j in range(N):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[N-1-i][j]
                matrix[N-1-i][j] = tmp

    for i in range(N):
        for j in range(N):
            if i > j:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# matrix = [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]

matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
rotate2(matrix)
for r in matrix:
    print(r)
