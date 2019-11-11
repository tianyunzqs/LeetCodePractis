# -*- coding: utf-8 -*-
# @Time        : 2019/11/11 18:47
# @Author      : tianyunzqs
# @Description : 

"""
120. Triangle
Medium

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


def minimumTotal(triangle) -> int:
    """
    程序运行过程：
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    j = 4
    res[0] = min(4, 1) + 6 = 7
    res[1] = min(1, 8) + 5 = 6
    res[2] = min(8, 3) + 7 = 10
    res[3] = 3

         [2],
        [3,4],
       [7,6,10,3]
    res[0] = min(7, 6) + 3 = 9
    res[1] = min(6, 10) + 4 = 10
    res[2] = 10
    res[3] = 3

         [2],
       [9,10,10,3]
    res[0] = min(9, 10) + 2 = 11
    res[1] = 10
    res[2] = 10
    res[3] = 3
    :param triangle:
    :return:
    """
    if not triangle:
        return 0

    res = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            res[j] = min(res[j], res[j + 1]) + triangle[i][j]
    return res[0]


if __name__ == '__main__':
    a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    a = [
         [-1],
         [2,3],
        [1,-1,-3]
    ]
    print(minimumTotal(a))
