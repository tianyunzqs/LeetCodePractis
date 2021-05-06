# -*- coding: utf-8 -*-
# @Time        : 2021/5/6 14:07
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/pascals-triangle-ii/
119. 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
"""

from typing import List


class Solution:
    def getRow1(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        result = []
        for row in range(rowIndex + 1):
            tmp = [1] * (row + 1)
            for j in range(row - 1):
                tmp[j + 1] = result[-1][j] + result[-1][j + 1]
            result.append(tmp)
        return result[-1]

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        result = []
        for row in range(rowIndex + 1):
            new_result = [1] * (row + 1)
            for j in range(row - 1):
                new_result[j + 1] = result[j] + result[j + 1]
            result = new_result[:]
        return result


if __name__ == '__main__':
    print(Solution().getRow1(3))
    print(Solution().getRow(3))
