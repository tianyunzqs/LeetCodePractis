# -*- coding: utf-8 -*-
# @Time        : 2019/7/5 15:18
# @Author      : tianyunzqs
# @Description : 

"""
1. Two Sum
Easy


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    """
    解题思路：遍历给定数组A，如果b = target - a 的值在已遍历完的部分中，那么返回a和b所在的下标。
    :param nums:
    :param target:
    :return:
    """
    d = {}
    for i, a in enumerate(nums):
        if target - a in d:
            return [d[target-a], i]
        d[a] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
