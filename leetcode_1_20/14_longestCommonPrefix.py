# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 15:33
# @Author      : tianyunzqs
# @Description ：

"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


def longestCommonPrefix(strs) -> str:
    if not strs:
        return ''
    common_char = set()
    common_prefix = ''
    min_len = min([len(item) for item in strs])
    for i in range(min_len):
        for char in strs:
            common_char.add(char[i])
        if len(common_char) == 1:
            common_prefix += common_char.pop()
        else:
            break
    return common_prefix


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))
