# -*- coding: utf-8 -*-
# @Time        : 2019/7/9 16:23
# @Author      : tianyunzqs
# @Description : 

"""
77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

import itertools


def combine1(n: int, k: int):
    """
    python自带的itertool工具中有combinations函数
    :param n:
    :param k:
    :return:
    """
    nums = list(range(1, n+1))
    # 组合，不考虑顺序
    a = list(itertools.combinations(nums, k))
    # 排列，考虑顺序
    # a = list(itertools.permutations(nums, k))
    return a


def combine2(n: int, k: int):
    """
    递归方式1
    当前结果是在上一次结果的基础上插入元素来实现的
    当n值较大时，运行时间较长
    :param n:
    :param k:
    :return:
    """
    nums = list(range(1, n+1))

    def fun(nums, k):
        if k == 1:
            return [[i] for i in nums]

        # 当前结果等于在前一次结果的基础上，插入其余元素的结果
        a = fun(nums, k-1)
        res = []
        for aa in a:
            for i in set(nums) - set(aa):
                tmp = aa + [i]
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
        return res

    return fun(nums, k)


def combine3(n: int, k: int):
    result = []
    tmp = [0] * k
    nums = range(1, n+1)

    def next_num(li=0, ni=0):
        if ni == k:
            result.append(list(tuple(tmp)))
            return
        for lj in range(li, n):
            tmp[ni] = nums[lj]
            next_num(lj+1, ni+1)

    next_num()
    return result


def permutation(lst,k):
    result = []
    tmp = [0]*k

    def next_num(a,ni=0):
        if ni == k:
            result.append(tuple(tmp))
            return
        for lj in a:
            tmp[ni] = lj
            b = a[:]
            b.pop(a.index(lj))
            next_num(b,ni+1)

    c = lst[:]
    next_num(c,0)
    return result


if __name__ == '__main__':
    # print(combine1(20, 16))
    # print(combine2(20, 16))
    print(combine3(4, 2))
    print(permutation([1, 2, 3, 4], 2))

