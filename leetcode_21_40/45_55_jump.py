# -*- coding: utf-8 -*-
# @Time        : 2019/6/26 9:29
# @Author      : tianyunzqs
# @Description : 

import sys


def jump_my(nums):

    def fun(nums2, rrr, t):
        if not nums2 or len(nums2) < 2:
            return 0
        elif len(nums2) == 2:
            return 1
        else:
            for step in range(1, nums2[0] + 1):
                t = fun(nums2[step:], rrr, t+step)
                rrr.append(t)
            return min(rrr)

    return fun(nums, [], 0)


def jump2(nums):
    """
    定义一个最远可达位置变量和下一次最远可达位置变量。
    其中，下一次最远可达位置变量在遍历数组的时候都需要更新，而最远可达位置变量只有在其与当前位置相等时才更新。
    :param nums:
    :return:
    """
    max_reach_idx, next_max_reach_idx, min_jumps, len_nums = 0, 0, 0, len(nums)

    for i, x in enumerate(nums):
        # 如果最远可达位置超过数组长度，则说明可以一步到位，直接返回即可
        if max_reach_idx >= len_nums - 1:
            return min_jumps

        # 更新下一次最远可达位置
        next_max_reach_idx = max(next_max_reach_idx, i + x)

        # 如果当前位置与最远可达位置重合，则更新最远位置为下一次最远可达位置
        if i == max_reach_idx:
            min_jumps = min_jumps + 1
            max_reach_idx = next_max_reach_idx


def canJump(nums):
    max_reach_idx, next_max_reach_idx, len_nums = 0, 0, len(nums)

    for i, x in enumerate(nums):
        # 如果最远可达位置超过数组长度，则说明可以一步到位，直接返回即可
        if max_reach_idx >= len_nums - 1:
            return True

        # 更新下一次最远可达位置
        next_max_reach_idx = max(next_max_reach_idx, i + x)

        # 如果当前位置与最远可达位置重合，则更新最远位置为下一次最远可达位置
        if i == max_reach_idx:
            max_reach_idx = next_max_reach_idx

    return False


nums = [2,3,1,1,4]
print(jump2(nums))

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(canJump(nums))
