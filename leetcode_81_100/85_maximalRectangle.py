# -*- coding: utf-8 -*-
# @Time        : 2019/7/18 11:09
# @Author      : tianyunzqs
# @Description : 

"""
85. Maximal Rectangle
Hard

Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""


def largestRectangleArea(heights):
    """
    :param heights:
    :return:
    """
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    heights.pop()
    return ans


def maximalRectangle(matrix) -> int:
    """
    遍历行，将下一行对应元素累加到上一行对应元素上，
    将问题转换为84题的最大面积问题
    :param matrix:
    :return:
    """
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * n
    ans = 0
    for row in matrix:
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        ans = max(ans, largestRectangleArea(height))
    return ans


if __name__ == '__main__':
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print(maximalRectangle(matrix))
