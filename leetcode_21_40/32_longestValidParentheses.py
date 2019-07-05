# -*- coding: utf-8 -*-
# @Time        : 2019/6/17 16:59
# @Author      : tianyunzqs
# @Description : 


def isValid(s: str) -> bool:
    if not s:
        return True
    char2int = {'(': 1, '{': 2, '[': 3, ')': -1, '}': -2, ']': -3}
    start_char_list = []
    for ch in s:
        ch2int = char2int[ch]
        if ch in ('(', '{', '['):
            start_char_list.append(ch2int)
        else:
            if not start_char_list:
                return False
            elif start_char_list[-1] != -ch2int:
                return False
            else:
                start_char_list.pop()
    if not start_char_list:
        return True
    else:
        return False


def longestValidParentheses(s: str) -> int:
    dp = [0] * len(s)  # dp[i] 表示第i个位置有效长度
    left_parentheses_list = []  # 存储左括号
    lvp = 0  # 最长有效括号数量
    for i, ch in enumerate(s):
        if ch == '(':
            left_parentheses_list.append(i)
        else:
            if left_parentheses_list and i > 0:
                dp[i] = dp[i-1] + 2 + dp[left_parentheses_list[-1] - 1]
                lvp = max(lvp, dp[i])
                left_parentheses_list.pop()

    return lvp


# s = ")()())"
# s = "(()"
# s = "()(()"
s = "())())(((())))"
print(longestValidParentheses(s))
