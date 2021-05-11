# -*- coding: utf-8 -*-
# @Time        : 2021/5/10 10:06
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/valid-palindrome/
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]+', '', s.lower())
        mid_idx = len(s) // 2
        if len(s) % 2:
            return s[:mid_idx] == s[mid_idx+1:][::-1]
        else:
            return s[:mid_idx] == s[mid_idx:][::-1]

    def isPalindrome2(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]+', '', s.lower())
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    print(Solution().isPalindrome('1'))
