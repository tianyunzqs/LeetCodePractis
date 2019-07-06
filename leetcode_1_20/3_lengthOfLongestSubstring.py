# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 15:27
# @Author      : tianyunzqs
# @Description ：

"""
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s: str) -> int:
    max_len, start = 0, 0
    d = {}
    for i, ch in enumerate(s):
        # 如果重复字符位置比开始位置小，则说明该字符并未在最长字串中，可以添加到字串，因为此使被重复的字符已被排除出字串
        if ch in d and d[ch] >= start:
            start = d[ch] + 1
        else:
            max_len = max(max_len, i - start + 1)
        d[ch] = i
    return max_len


if __name__ == '__main__':
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))
