# -*- coding: utf-8 -*-
# @Time        : 2019/7/28 23:00
# @Author      : tianyunzqs
# @Description ：

"""
97. Interleaving String
Hard

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    """
    递归解法，TLE（Time Limit Exceeded）
    :param s1:
    :param s2:
    :param s3:
    :return:
    """
    if len(s3) != len(s1 + s2):
        return False
    if not s1 or not s2:
        return s3 == s1 + s2
    if s3 == s1 + s2 or s3 == s2 + s1:
        return True

    i, j, k = 0, 0, 0
    while k < len(s3):
        if s3[k] == s1[i] and s3[k] != s2[j]:
            i += 1
            k += 1
            return isInterleave(s1[i:], s2, s3[k:])
        elif s3[k] != s1[i] and s3[k] == s2[j]:
            j += 1
            k += 1
            return isInterleave(s1, s2[j:], s3[k:])
        elif s3[k] == s1[i] and s3[k] == s2[j]:
            i += 1
            j += 1
            k += 1
            return isInterleave(s1[i:], s2, s3[k:]) or isInterleave(s1, s2[j:], s3[k:])
        else:
            return False


def isInterleave2(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1 + s2):
        return False

    dp = [True for _ in range(len(s1) + 1)]
    for i in range(len(s1)):
        dp[i + 1] = dp[i] and s1[i] == s3[i]

    for j in range(1, len(s2) + 1):
        dp[0] = dp[0] and s2[j - 1] == s3[j - 1]
        for i in range(1, len(s1) + 1):
            dp[i] = dp[i - 1] and s1[i - 1] == s3[i + j - 1] or dp[i] and s2[j - 1] == s3[i + j - 1]

    return dp[len(s1)]


def isInterleave3(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1 + s2):
        return False

    dp = [[True for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            else:
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[len(s1)][len(s2)]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"

    s1 = "a"
    s2 = ""
    s3 = "c"

    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    # print(isInterleave(s1, s2, s3))
    print(isInterleave2(s1, s2, s3))
    print(isInterleave3(s1, s2, s3))
