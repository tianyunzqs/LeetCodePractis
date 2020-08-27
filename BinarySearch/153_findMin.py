# -*- coding: utf-8 -*-
# @Time        : 2020/8/27 22:10
# @Author      : tianyunzqs
# @Description ：

"""
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""

from typing import List


class Solution:
    """
    二分查找，寻找最小值
    """
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        # 如果第一个数比最后一个数小，说明nums未旋转
        if nums[0] < nums[-1]:
            return nums[0]
        i, j = 0, len(nums) - 1
        # 从前后同时向中间搜索
        while i < j:
            if nums[i] > nums[j]:  # 可以继续试探
                i += 1
                j -= 1
            else:  # 找到了最小值
                # 如果前向当前值比上一次的后向值小（隐含着比后向当前值小，因为进入else了），则最小值就是前向当前值
                return nums[i] if nums[i] < nums[j+1] else nums[j+1]
        if i == j:  # 最小值等于当前指针指向的值与后一个值的较小者
            return nums[i] if nums[i] < nums[i+1] else nums[i+1]
        else:  # i > j 说明最小值就是nums[i]
            return nums[i]


if __name__ == '__main__':
    print(Solution().findMin([1]))
    print(Solution().findMin([1, 2]))
    print(Solution().findMin([2, 1]))
    print(Solution().findMin([1, 2, 3]))
    print(Solution().findMin([3,4,5,1,2]))
    print(Solution().findMin([2, 3, 4, 5, 1]))
    print(Solution().findMin([4,5,6,7,0,1,2]))
    print(Solution().findMin([6, 0, 1, 2, 3, 4, 5]))

