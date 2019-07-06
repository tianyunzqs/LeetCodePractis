# -*- coding: utf-8 -*-
# @Time        : 2019/4/8 22:47
# @Author      : tianyunzqs
# @Description ：

"""
7. Reverse Integer
Easy


Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


def reverse(x: int) -> int:
    # x = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
    # return x if -2 ** 31 <= x <= (2 ** 31 - 1) else 0

    flag = -1 if x < 0 else 1
    x = abs(x)
    result = 0
    if -2**31 <= x <= 2**31 - 1:
        while x:
            result = (x % 10) + 10 * result
            x = x // 10
    if -2 ** 31 <= result * flag <= 2 ** 31 - 1:
        return result * flag
    else:
        return 0


if __name__ == '__main__':
    print(reverse(1534236469))
