# -*- coding: utf-8 -*-
# @Time        : 2019/7/3 9:44
# @Author      : tianyunzqs
# @Description : 

"""
69. Sqrt(x)
Easy


Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


def mySqrt(x: int) -> int:
    def fun(x, d_min, d_max):
        if d_max == d_min or (d_max - d_min == 1 and d_min * d_min <= x < d_max * d_max):
            return d_min

        mid = (d_min + d_max) // 2

        if x < mid * mid:
            res = fun(x, d_min, mid)
        else:
            res = fun(x, mid, d_max)

        return res

    return fun(x, 1, x)


print(mySqrt(2000000000000))
