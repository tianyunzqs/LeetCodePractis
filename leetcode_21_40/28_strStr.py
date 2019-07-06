# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 18:22
# @Author      : tianyunzqs
# @Description ：

"""
28. Implement strStr()
Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""


def strStr(haystack: str, needle: str) -> int:
    # # solution1
    # try:
    #     return haystack.index(needle)
    # except:
    #     return -1

    # solution2
    if not needle or haystack == needle:
        return 0
    if not haystack:
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


if __name__ == '__main__':
    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack, needle))
