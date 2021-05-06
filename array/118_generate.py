# -*- coding: utf-8 -*-
# @Time        : 2021/5/6 13:49
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/pascals-triangle/
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        result = []
        for row in range(numRows):
            tmp = [1] * (row + 1)
            for j in range(row - 1):
                tmp[j + 1] = result[-1][j] + result[-1][j + 1]
            result.append(tmp)
        return result


if __name__ == '__main__':
    res = Solution().generate(8)
    for r in res:
        print(r)
