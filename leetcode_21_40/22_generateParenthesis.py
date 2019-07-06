# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 18:17
# @Author      : tianyunzqs
# @Description ：

"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generateParenthesis(n: int):
    res = []
    s = [("(", 1, 0)]
    while s:
        x, l, r = s.pop()
        if l - r < 0 or l > n or r > n:
            continue
        if l == n and r == n:
            res.append(x)
        s.append((x + "(", l + 1, r))
        s.append((x + ")", l, r + 1))
    return res


if __name__ == '__main__':
    print(generateParenthesis(3))
