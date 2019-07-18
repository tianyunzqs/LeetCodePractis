# -*- coding: utf-8 -*-
# @Time        : 2019/7/18 16:33
# @Author      : tianyunzqs
# @Description : 


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


def subsetsWithDup(nums):
    """
    利用组合来产生各个长度的组合集合
    :param nums:
    :return:
    """
    nums.sort()
    res = list()
    for i in range(len(nums) + 1):
        for r in combine(nums, i):
            if r not in res:
                res.append(r)
    return res


def subsetsWithDup2(nums):
    """
    从空到1到2，...，一直到nums，不断在前面结果的基础上产生新的组合
    :param nums:
    :return:
    """
    res = [[]]
    nums.sort()
    for num in nums:
        # tmp = []
        # for r in res:
        #     tmp += [r + [num]]
        # res += tmp
        res += [i + [num] for i in res if i + [num] not in res]
    return res


if __name__ == '__main__':
    nums = [1, 2, 2]
    print(subsetsWithDup(nums))
    print(subsetsWithDup2(nums))
