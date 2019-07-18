# -*- coding: utf-8 -*-
# @Time        : 2019/7/18 17:34
# @Author      : tianyunzqs
# @Description : 

"""
91. Decode Ways
Medium

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


def numDecodings(s: str) -> int:
    if len(s) == 0 or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        return 2 if int(s) <= 26 and '0' not in s else 1

    dp = [0 for _ in range(len(s))]
    dp[0] = 1 if s[0] != '0' else 0
    if int(s[:2]) > 26 and s[1] == '0':
        return 0
    else:
        dp[1] = dp[0] if int(s[:2]) > 26 or s[1] == '0' else dp[0] + 1
    for i in range(2, len(s)):
        if s[i] == '0':
            if int(s[i - 1:i + 1]) <= 26:
                dp[i] = dp[i-1]
            else:
                return 0
        elif 0 < int(s[i-1:i+1]) <= 26 and s[i-1] != '0':
            dp[i] = dp[i-2] + dp[i-1]
        else:
            dp[i] = dp[i-1]

    return dp[-1]


if __name__ == '__main__':
    print(numDecodings("0"))
    print(numDecodings("10"))
    print(numDecodings("01"))
    print(numDecodings("101"))
    print(numDecodings("110"))
    print(numDecodings("1010"))
