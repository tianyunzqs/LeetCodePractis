# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 15:35
# @Author      : tianyunzqs
# @Description ：

"""
20. Valid Parentheses
Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


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


if __name__ == '__main__':
    s = "()[]{}"
    print(isValid(s))
