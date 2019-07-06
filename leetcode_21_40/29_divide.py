# -*- coding: utf-8 -*-
# @Time        : 2019/6/16 14:10
# @Author      : tianyunzqs
# @Description ：

"""
29. Divide Two Integers
Medium

Given two integers dividend and divisor, divide two integers without using multiplication,
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1
when the division result overflows.
"""


def divide(dividend: int, divisor: int) -> int:
    flag = (dividend >= 0) ^ (divisor > 0)  # 判断除数或被除数是否有负数
    dividend, divisor = abs(dividend), abs(divisor)
    result = 0
    while dividend >= divisor:
        index2 = 1           # 以2的指数形式增长，加快计算速度
        div_tmp = divisor    # 除数每次在原来的基础上乘以2
        while dividend >= div_tmp:    # 说明还可以进行除法运算
            dividend -= div_tmp
            result += index2
            index2 = index2 << 1
            div_tmp = div_tmp << 1

    return min(result, 2 ** 31 - 1) if not flag else max(-result, -(2 ** 31))


if __name__ == '__main__':
    print(divide(10, 3))
