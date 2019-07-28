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
    print(isInterleave(s1, s2, s3))
