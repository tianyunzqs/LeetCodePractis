# -*- coding: utf-8 -*-
# @Time        : 2019/6/25 10:35
# @Author      : tianyunzqs
# @Description : 


def multiply(num1: str, num2: str):
    num1, num2 = num1[::-1], num2[::-1]
    total = 0
    d = 1
    for i in num2:
        carry = 0
        d1 = d
        for j in num1:
            a = (int(i) * int(j) + carry) % 10
            carry = (int(i) * int(j) + carry) // 10
            total += a * d1
            d1 *= 10
        if carry:
            total += carry * d1
        d *= 10

    return total


num1 = "1234"
num2 = "456"
# "56088"
multiply(num1, num2)
