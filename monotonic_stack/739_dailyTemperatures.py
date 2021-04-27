# -*- coding: utf-8 -*-
# @Time        : 2019/11/19 22:59
# @Author      : tianyunzqs
# @Description ：

"""
739. Daily Temperatures
Medium

Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""


def dailyTemperatures(T):
    # 单调递增栈
    in_stk = []
    res = [0] * len(T)
    for i, t in enumerate(T):
        while in_stk and T[in_stk[-1]] < t:
            res[in_stk[-1]] = i - in_stk[-1]
            in_stk.pop()
        in_stk.append(i)

    return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))
