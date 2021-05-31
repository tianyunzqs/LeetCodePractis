# -*- coding: utf-8 -*-
# @Time        : 2021/5/31 10:21
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/longest-consecutive-sequence/
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

提示：
0 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def find(self, x, fa):
        if x == fa[x]:
            return x
        else:
            fa[x] = self.find(fa[x], fa)
            return fa[x]

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        result = [[nums[0]]]
        i = 0
        while i < len(nums) - 1:
            if nums[i] + 1 == nums[i + 1]:
                result[-1].append(nums[i + 1])
            else:
                result.append([nums[i + 1]])
            i += 1
        return max([len(r) for r in result])

    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        result = [[nums[0]]]
        i = 0
        while i < len(nums) - 1:
            if nums[i] + 1 == nums[i + 1]:
                result[-1].append(nums[i + 1])
            else:
                result.append([nums[i + 1]])
            i += 1
        return max([len(r) for r in result])


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(Solution().longestConsecutive(nums))
