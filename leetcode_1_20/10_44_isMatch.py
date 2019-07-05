# -*- coding: utf-8 -*-
# @Time        : 2019/6/12 10:12
# @Author      : tianyunzqs
# @Description : 

"""
10. Regular Expression Matching
Hard


Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


def isMatch_10(s, p):
    m, n = len(s), len(p)
    # dp[i][j] 表示p[:j]是否匹配s[:i]的结果（如果能匹配，则dp[i][j]=True，否则dp[i][j]=False）
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    # 先计算一些特殊情况，如dp[0][0], dp[0][j], dp[i][0]
    dp[0][0] = True   # s[:0] = ''  p[:0] = ''  匹配
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    # dp[i][0] 表示s不为空，而p为空，则不匹配（i>0），可以不用写，已初始化过
    # for i in range(1, len(s)+1):
    #     dp[i][0] = False

    # 考虑为空的情形
    s = ' ' + s
    p = ' ' + p

    # 计算一般情况
    for i in range(1, m+1):
        for j in range(1, n+1):
            # s[:i] = '(string)a' p[:j] = '(re_string)a' or '(re_string).'
            if s[i] == p[j] or p[j] == '.':
                dp[i][j] = dp[i-1][j-1]
            # s[:i] = '(string)a' p[:j] = '(re_string)*'
            elif p[j] == '*':
                if j > 1:   # (a, ab*)   很粗的规则
                    dp[i][j] = dp[i][j-2]
                if p[j-1] == s[i] or p[j-1] == '.':   # [(ab, ab*), (ab, a.*)]   精细的规则，所以加上或操作
                    dp[i][j] |= dp[i-1][j]

    return dp[-1][-1]


"""
44. Wildcard Matching
Hard


Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


def isMatch_44(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    # dp[i][j] 表示p[:j]是否匹配s[:i]的结果（如果能匹配，则dp[i][j]=True，否则dp[i][j]=False）
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    # 先计算一些特殊情况，如dp[0][0], dp[0][j], dp[i][0]
    dp[0][0] = True  # s[:0] = ''  p[:0] = ''  匹配
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    # dp[i][0] 表示s不为空，而p为空，则不匹配（i>0），可以不用写，已初始化过
    # for i in range(1, len(s)+1):
    #     dp[i][0] = False

    # 考虑为空的情形
    s = ' ' + s
    p = ' ' + p

    # 计算一般情况
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # s[:i] = '(string)a' p[:j] = '(re_string)a' or '(re_string).'
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            # s[:i] = '(string)a' p[:j] = '(re_string)*'
            elif p[j] == '*':
                dp[i][j] = dp[i - 1][j] | dp[i][j - 1]

    return dp[-1][-1]


if __name__ == '__main__':
    # s = 'ssissippi'
    # p = 's*is*ip*.'
    # print(isMatch_10(s, p)

    s = "aa"
    p = "a"
    print(isMatch_44(s, p))
