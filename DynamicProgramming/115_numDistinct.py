# -*- coding: utf-8 -*-
# @Time        : 2019/10/30 16:33
# @Author      : tianyunzqs
# @Description : 

"""
115. Distinct Subsequences
Hard


Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""


def numDistinct(s: str, t: str) -> int:
    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
    for j in range(len(s)+1):
        dp[0][j] = 1

    for i in range(len(t)):
        for j in range(len(s)):
            if s[j] == t[i]:
                dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
            else:
                dp[i + 1][j + 1] = dp[i+1][j]

    for a in dp:
        print(a)
    return dp[-1][-1]


if __name__ == '__main__':
    S = "rabbbit"
    T = "rabbit"
    print(numDistinct(S, T))
    S = "babgbag"
    T = "bag"
    print(numDistinct(S, T))
