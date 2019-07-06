# -*- coding: utf-8 -*-
# @Time        : 2019/6/21 23:09
# @Author      : tianyunzqs
# @Description ：

"""
38. Count and Say
Easy


The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


def fun(n_str):
    result = ''
    cur_str, num = n_str[0], 1
    for s in n_str[1:]:
        if s == cur_str:
            num += 1
        else:
            result += str(num) + cur_str
            cur_str, num = s, 1
    result += str(num) + cur_str
    return result


def countAndSay(n):
    if n == 1:
        return '1'
    else:
        return fun(countAndSay(n - 1))


if __name__ == '__main__':
    print(countAndSay(7))
