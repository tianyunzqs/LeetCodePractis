# -*- coding: utf-8 -*-
# @Time        : 2019/6/12 10:12
# @Author      : tianyunzqs
# @Description : 


def isMatch2(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    if s == p:
        return True

    # INITIALIZING

    # 2
    m = len(s)
    # 1
    n = len(p)

    T = [[False for j in range(n + 1)] for i in range(m + 1)]

    T[0][0] = True

    #  Deals with patterns like a* or a*b* or a*b*c*
    for i in range(1, n + 1):
        if p[i - 1] == '*':
            T[0][i] = T[0][i - 2]

    if not s:
        return T[-1][-1]

    s = " " + s
    p = " " + p

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s[i] == p[j] or p[j] == '.':
                T[i][j] = T[i - 1][j - 1]


            elif p[j] == '*':
                if j > 1:
                    T[i][j] = T[i][j - 2]

                if s[i] == p[j - 1] or p[j - 1] == '.':
                    T[i][j] = T[i][j] or T[i - 1][j]
            else:
                T[i][j] = False

    return T[i][j]


def isMatch(s, p):
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


def isMatch44(s: str, p: str) -> bool:
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
    # print(isMatch2(s, p)
    # print(isMatch(s, p))

    s = "aa"
    p = "a"
    print(isMatch44(s, p))
