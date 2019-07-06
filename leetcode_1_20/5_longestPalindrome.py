# -*- coding: utf-8 -*-
# @Time        : 2019/4/8 20:54
# @Author      : tianyunzqs
# @Description ：

"""
5. Longest Palindromic Substring
Medium


Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def longestPalindrome(s: str) -> str:

    def is_palindrome(s: str):
        half = len(s) // 2
        if len(s) % 2:
            if s[:half] == s[half + 1:][::-1]:
                return True
        else:
            if s[:half] == s[half:][::-1]:
                return True
        return False

    if not s:
        return s
    char_ind = {}
    for i, ch in enumerate(s):
        if ch not in char_ind:
            char_ind[ch] = [i]
        else:
            char_ind[ch].append(i)
    char_ind2 = filter(lambda x: len(x[1]) > 1, char_ind.items())
    result = []
    for char, inds in char_ind2:
        for i1 in inds:
            for i2 in inds:
                if i1 < i2 and is_palindrome(s[i1:i2+1]):
                    result.append(s[i1:i2+1])
    if result:
        return sorted(result, key=lambda x: len(x), reverse=True)[0]
    else:
        return s[0]


if __name__ == '__main__':
    print(longestPalindrome('cbbd'))
