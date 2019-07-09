# -*- coding: utf-8 -*-
# @Time        : 2019/7/9 10:43
# @Author      : tianyunzqs
# @Description : 

"""
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


def searchMatrix(matrix, target: int) -> bool:
    """
    首先确定目标值可能所在的行，判断条件是：大于等于改行第一个元素，并且小于等于改行最后一个元素
    确定行后，在该行定义从前往后和从后往前的两个指针，直至两个指针相遇，如果找到返回True，否则返回False
    :param matrix:
    :param target:
    :return:
    """
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    candidate_row = -1
    for i in range(m):
        if matrix[i][0] <= target <= matrix[i][-1]:
            candidate_row = i
            break
    if candidate_row == -1:
        return False

    left, right = 0, n-1
    while left <= right:
        if matrix[candidate_row][left] == target or matrix[candidate_row][right] == target:
            return True
        elif matrix[candidate_row][left] < target:
            left += 1
        elif matrix[candidate_row][right] > target:
            right -= 1
    return False


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3

    matrix = [
        [1],
        [3]
    ]
    target = 3
    print(searchMatrix(matrix, target))
