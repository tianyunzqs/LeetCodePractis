# -*- coding: utf-8 -*-
# @Time        : 2021/6/1 10:04
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/circle/discuss/vMYOmI/
已知一个无序数组 array，元素均为正整数。给定一个目标值 target，输出数组中是否存在若干元素的组合，相加为目标值。

对于以下无序数组
candidates = [3, 9, 5, 8, 7, 17]
target = 16
输出
[[3, 5, 8],
[9, 7]]
"""

from typing import List


class Solution:
    def sumTarget(self, candidates: List[int], target: int) -> List[List[int]]:
        def fun(candidates, target, res):
            if not candidates or target < min(candidates) or target > sum(candidates):
                return []
            for i, num in enumerate(candidates):
                res.append(num)
                if num == target:
                    result.append(res[:])
                fun(candidates[i + 1:], target - num, res)
                res.pop()

        result = []
        fun(candidates, target, [])
        return [list(r) for r in set([tuple(sorted(item)) for item in result])]


if __name__ == '__main__':
    candidates = [3, 9, 5, 8, 7, 17]
    target = 46
    for t in range(57):
        print(t, Solution().sumTarget(candidates, t))
