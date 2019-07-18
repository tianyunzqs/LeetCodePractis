# -*- coding: utf-8 -*-
# @Time        : 2019/7/18 14:24
# @Author      : tianyunzqs
# @Description : 

"""
87. Scramble String
Hard

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false
"""


def isScramble(s1: str, s2: str) -> bool:
    """
    如果s1和s2是 scramble 的话，
    那么必然存在一个在 s1 上的长度 l1，将 s1 分成 s11 和 s12 两段，
    同样有 s21 和 s22，
    那么要么 s11 和 s21 是 scramble 的并且 s12 和 s22 是 scramble 的；
    要么 s11 和 s22 是 scramble 的并且 s12 和 s21 是 scramble 的。
    就拿题目中的例子 rgeat 和 great 来说，
    rgeat 可分成 rg 和 eat 两段， great 可分成 gr 和 eat 两段，
    rg 和 gr 是 scrambled 的， eat 和 eat 当然是 scrambled。
    :param s1:
    :param s2:
    :return:
    """
    m, n = len(s1), len(s2)
    if m != n:
        return False
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    for i in range(1, m):
        s11, s12 = s1[:i], s1[i:]
        s21, s22 = s2[:i], s2[i:]
        if isScramble(s11, s21) and isScramble(s12, s22):
            return True
        s21, s22 = s2[m-i:], s2[:m-i]
        if isScramble(s11, s21) and isScramble(s12, s22):
            return True

    return False


if __name__ == '__main__':
    s1 = "great"
    s2 = "rgeat"
    print(isScramble(s1, s2))
