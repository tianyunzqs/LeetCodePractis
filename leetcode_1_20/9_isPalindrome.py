# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 15:30
# @Author      : tianyunzqs
# @Description ：

"""
9. Palindrome Number
Easy

Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""


def isPalindrome(x: int) -> bool:
    # # 转换成字符串的形式
    # s = str(x)
    # # 以下等价于：return True if s == s[:,:,-1] else False
    # half = len(s) // 2
    # if len(s) % 2:
    #     if s[:half] == s[half + 1:][::-1]:
    #         return True
    # else:
    #     if s[:half] == s[half:][::-1]:
    #         return True
    # return False

    # 不转换成字符串的形式（为什么会产生超时？？？）
    if x < 0:
        return False

    origin_x, reverse_x = x, 0
    while x:
        reverse_x = (x % 10) + 10 * reverse_x
        x = x // 10

    return True if origin_x == reverse_x else False


if __name__ == '__main__':
    print(isPalindrome(10))
