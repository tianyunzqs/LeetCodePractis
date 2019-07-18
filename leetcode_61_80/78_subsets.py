# -*- coding: utf-8 -*-
# @Time        : 2019/7/10 9:06
# @Author      : tianyunzqs
# @Description : 

"""
78. Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def combine(nums: list, k: int):
    """
    产生组合递归实现方式
    :param nums:
    :param k:
    :return:
    """
    result = []
    tmp = [0] * k
    n = len(nums)

    def next_num(li=0, ni=0):
        if ni == k:
            result.append(list(tuple(tmp)))
            return
        for lj in range(li, n):
            tmp[ni] = nums[lj]
            next_num(lj+1, ni+1)

    next_num()
    return result


def subsets(nums):
    res = list()
    for i in range(len(nums) + 1):
        res += combine(nums, i)
    return res


def subsets2(nums):
    res = [[]]
    nums.sort()
    for num in nums:
        # tmp = []
        # for r in res:
        #     tmp += [r + [num]]
        # res += tmp
        res += [i + [num] for i in res]
    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(subsets(nums))
    print(subsets2(nums))
