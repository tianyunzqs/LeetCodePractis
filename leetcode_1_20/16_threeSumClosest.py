# -*- coding: utf-8 -*-
# @Time        : 2019/6/10 14:16
# @Author      : tianyunzqs
# @Description : 

import sys


def twoSum(nums: list, target: int):
    """
    给定数组nums和target，返回a+b=target，其中a,b∈nums
    nums = [-1, 2, 1, 4, 3, 0, 2]
    target = 4
    [
        [2, 2],
        [1, 3],
        [0, 4]
    ]
    :param nums:
    :param target:
    :return:
    """
    result = set()
    nums_sorted = sorted(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        if nums_sorted[left] + nums_sorted[right] == target:
            result.add((nums_sorted[left], nums_sorted[right]))
            left += 1
        elif nums_sorted[left] + nums_sorted[right] < target:
            left += 1
        else:
            right -= 1

    return [list(item) for item in result]


def twoSumClosest(nums: list, target: int):
    """
    给定数组nums和target，返回a+b，使其值最接近target，其中a,b∈nums，假设每个输入都存在一个输出解
    nums = [-1, 2, 1, -4]
    target = 2
    返回：-1+2 = 1
    :param nums:
    :param target:
    :return:
    """
    nums_sorted = sorted(nums)
    left, right = 0, len(nums) - 1

    diff = total = sys.maxsize
    while left < right:
        new_diff = abs(nums_sorted[left] + nums_sorted[right] - target)
        if new_diff < diff:
            diff = new_diff
            total = nums_sorted[left] + nums_sorted[right]
            left += 1
        else:
            right -= 1

    return total


def threeSum(nums: list, target: int):
    """
    给定数组nums和target，返回a+b+c=target，其中a,b,c∈nums
    nums = [-1, 2, 1, 4, 3, 0, 2]
    target = 4
    [
        [2, 2],
        [1, 3],
        [0, 4]
    ]
    :param nums:
    :param target:
    :return:
    """
    result = set()
    nums_sorted = sorted(nums)
    for i in range(len(nums_sorted)):
        left, right = i + 1, len(nums_sorted) - 1
        while left < right:
            total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
            if total == target:
                result.add((nums_sorted[i], nums_sorted[left], nums_sorted[right]))
                left += 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return [list(item) for item in result]


def threeSum2(nums: list, target: int):
    """
    给定数组nums和target，返回a+b+c=target，其中a,b,c∈nums
    nums = [-1, 2, 1, 4, 3, 0, 2]
    target = 4
    [
        [2, 2],
        [1, 3],
        [0, 4]
    ]
    :param nums:
    :param target:
    :return:
    """
    result = set()
    nums_sorted = sorted(nums)
    for i in range(len(nums_sorted)):
        left, right = i + 1, len(nums_sorted) - 1
        while left < right:
            if nums_sorted[left] + nums_sorted[right] == target - nums_sorted[i]:
                result.add((nums_sorted[i], nums_sorted[left], nums_sorted[right]))
                left += 1
            elif nums_sorted[left] + nums_sorted[right] < target - nums_sorted[i]:
                left += 1
            else:
                right -= 1

    return [list(item) for item in result]


def threeSumClosest(nums: list, target: int):
    """
    给定数组nums和target，返回a+b，使其值最接近target，其中a,b∈nums，假设每个输入都存在一个输出解
    nums = [-1, 2, 1, -4]
    target = 2
    返回：-1+2 = 1
    :param nums:
    :param target:
    :return:
    """
    nums_sorted = sorted(nums)

    result = 0
    diff = sys.maxsize
    for i in range(len(nums_sorted)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
            new_diff = abs(total - target)

            if not new_diff:
                return total

            if new_diff < diff:
                diff = new_diff
                result = total

            if total < target:
                left += 1
            else:
                right -= 1

    return result


def fourSum(nums: list, target: int):
    result = set()
    nums_sorted = sorted(nums)
    for i in range(len(nums_sorted) - 2):
        three_result = threeSum2(nums_sorted[i+1:], target-nums_sorted[i])
        for tr in three_result:
            result.add(tuple([nums_sorted[i]] + tr))

    return [list(item) for item in result]


# a = [-1, 2, 1, 4, 3, 0, 2]
# a = [0, 0, 0, 0, 0, 0]
a = [-4, -3, -2, -1, 0, 0, 1, 2, 3, 4]
# a = [1, 0, -1, 0, -2, 2]
t = 0
print(fourSum(a, t))
