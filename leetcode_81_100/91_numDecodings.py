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


def numDecodings2(s: str) -> int:
    if len(s) == 0 or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1

    dp = [0 for _ in range(len(s))]
    dp[0] = 1 if s[0] != '0' else 0
    if int(s[:2]) > 26 and s[1] == '0':
        return 0
    else:
        dp[1] = dp[0] if int(s[:2]) > 26 or s[1] == '0' else dp[0] + 1

    for i in range(2, len(s)):
        if s[i] == '0':
            if int(s[i - 1:i + 1]) <= 26 and s[i-1] != '0':
                dp[i] = dp[i-2]
            else:
                return 0
        elif int(s[i-1:i+1]) <= 26 and s[i-1] != '0':
            dp[i] = dp[i-2] + dp[i-1]
        else:
            dp[i] = dp[i-1]

    return dp[-1]


def numDecodings3(s: str) -> int:
    if len(s) == 0 or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1

    dp = [0 for _ in range(len(s))]
    dp[0] = 1 if s[0] != '0' else 0
    if int(s[:2]) > 26 and s[1] == '0':
        return 0
    else:
        dp[1] = dp[0] if int(s[:2]) > 26 or s[1] == '0' else dp[0] + 1

    for i in range(2, len(s)):
        # '40','00'排除这两种可能
        if s[i] == '0' and (int(s[i-1]) > 2 or s[i-1] == '0'):
            return 0

        if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
            # '10'，'20'这两种情形dp[i] = dp[i-2]，'11'，'23'等情形dp[i] = dp[i-2] + dp[i-1]
            dp[i] = dp[i - 2] if s[i] == '0' else dp[i - 2] + dp[i - 1]
        else:
            dp[i] = dp[i - 1]

    return dp[-1]


def numDecodings(s):
    if not s:
        return 0

    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, len(s) + 1):
        if s[i-1] != '0':
            dp[i] += dp[i - 1]
        if s[i-2] != '0' and int(s[i-2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[len(s)]


if __name__ == '__main__':
    # 右对齐，5个字符长度
    print('{:>5}{:>2}'.format("0", numDecodings("0")))
    print('{:>5}{:>2}'.format("1", numDecodings("1")))
    print('{:>5}{:>2}'.format("10", numDecodings("10")))
    print('{:>5}{:>2}'.format("01", numDecodings("01")))
    print('{:>5}{:>2}'.format("101", numDecodings("101")))
    print('{:>5}{:>2}'.format("100", numDecodings("100")))
    print('{:>5}{:>2}'.format("1010", numDecodings("1010")))
    print('{:>5}{:>2}'.format("1111", numDecodings("1111")))
    print('{:>5}{:>2}'.format("30", numDecodings("30")))
    print('{:>5}{:>2}'.format("262", numDecodings("262")))
