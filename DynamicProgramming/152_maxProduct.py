# -*- coding: utf-8 -*-
# @Time        : 2020/5/12 19:04
# @Author      : tianyunzqs
# @Description : 

"""
152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution:
    def maxProduct(self, nums: list) -> int:
        max_product = nums[0]
        imax, imin = 1, 1
        for i, num in enumerate(nums):
            # 如果num为负数，那么之前的最大值乘以负数就成了最小值，故需要交换
            if num < 0:
                imax, imin = imin, imax
            # imax主要是记录到nums[i-1]的最大值，
            # 当运行到nums[i]时，有两种选择：
            # 1.将当前数nums[i]累乘到imax；
            # 2.重新开始
            imax = max(imax * num, num)
            # imin主要是为了防止负数的存在，对最大值的影响
            imin = min(imin * num, num)

            max_product = max(max_product, imax)

        return max_product


if __name__ == '__main__':
    print(Solution().maxProduct([2, 3, -2, 4, 0, 2, -3]))
    print(Solution().maxProduct([-2, 0, -1]))
    print(Solution().maxProduct([-2, 0, -2, 5]))
