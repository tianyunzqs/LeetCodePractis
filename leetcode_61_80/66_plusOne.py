# -*- coding: utf-8 -*-
# @Time        : 2019/7/2 15:53
# @Author      : tianyunzqs
# @Description : 

"""
66. Plus One
Easy


Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


# solution1
def plusOne(digits):
    num = int(''.join([str(d) for d in digits]))
    return [int(s) for s in str(num+1)]


# solution2
def plusOne2(digits):
    result = []
    digits = digits[::-1]
    result.append((digits[0] + 1) % 10)
    carry = (digits[0] + 1) // 10
    for d in digits[1:]:
        result.append((d + carry) % 10)
        carry = (d + carry) // 10

    if carry:
        result.append(carry)

    return result[::-1]


digits = [1,2,3]
digits = [9,9,9]
digits = [9,8,7,6,5,4,3,2,1,0]
# digits = [0]
print(plusOne(digits))
print(plusOne2(digits))
