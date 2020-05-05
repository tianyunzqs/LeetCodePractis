# -*- coding: utf-8 -*-
# @Time        : 2020/5/3 10:11
# @Author      : tianyunzqs
# @Description : 

"""
132. Palindrome Partitioning II
Hard

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


def is_palindrome_string(s: str) -> bool:
    return s == s[::-1]


def minCut(s: str) -> int:
    """
    dp[i]表示子串s[0:i+1]的最小切分次数
    最坏情况是切分len(s)-1次，此时任何子串均不能构成回文子串，故dp = [i for i in range(n)]
    在子串s[0:i+1]中寻找回文串，该回文串需以s[i+1]结尾，因为在其他位置的情况已在之前考虑过第一层for循环
    如果子串s[0:i+1]中存在以s[j]开头，以s[i+1]结尾的回文子串，则更新
    dp[i] = 0 if j = 0
    dp[i] = dp[j-1] + 1 if j > 0
    其中dp[j-1]表示s[0：j]的最小切分次数，+1表示回文子串s[j:i+1]
    a: 0
    ab: 1
    abc: 2
    abcc: 2
    abccb: 1
    abccba: 0
    abccbaa: 1
    abccbaab: 2
    abccbaabc: 3
    :param s:
    :return:
    """
    n = len(s)
    dp = [i for i in range(n)]
    for i in range(n):
        dp[i] = i
        for j in range(i + 1):
            if is_palindrome_string(s[j: i + 1]):
                dp[i] = 0 if j == 0 else min(dp[i], 1 + dp[j - 1])
    return dp[n - 1]


if __name__ == '__main__':
    # s = "aab"
    # s = "abacab"
    # s = "abccbab"
    s = "abccbaabc"
    print(minCut(s))
    # print(is_palindrome_string("abcdcba"))
