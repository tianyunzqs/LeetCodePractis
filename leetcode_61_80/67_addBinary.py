# -*- coding: utf-8 -*-
# @Time        : 2019/7/2 16:16
# @Author      : tianyunzqs
# @Description : 

"""
67. Add Binary
Easy


Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


def addBinary(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a = '0' * (max_len - len(a)) + a
    b = '0' * (max_len - len(b)) + b
    result = []
    carry = 0
    for i, j in zip(a[::-1], b[::-1]):
        i, j = int(i), int(j)
        result.append((i+j+carry) % 2)
        carry = (i+j+carry) // 2

    if carry:
        result.append(carry)

    return ''.join([str(d) for d in result[::-1]])


a = "11"
b = "1"

# a = "1010"
# b = "1011"
print(addBinary(a, b))
