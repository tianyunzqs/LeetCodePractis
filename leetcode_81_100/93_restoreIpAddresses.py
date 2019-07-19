# -*- coding: utf-8 -*-
# @Time        : 2019/7/19 11:25
# @Author      : tianyunzqs
# @Description : 

"""
93. Restore IP Addresses
Medium

Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


def is_valid(s):
    if s and 0 <= int(s) <= 255 and str(int(s)) == s:
        return True
    return False


def dfs(s, tmp, res, count):
    if count == 4 and is_valid(s):
        res.append(tmp + s)
        return
    for i in range(1, min(4, len(s))):
        cur = s[:i]
        if is_valid(cur):
            dfs(s[i:], tmp + cur + '.', res, count + 1)


def restoreIpAddresses(s: str):
    """
    递归解法，深度优先遍历
    :param s:
    :return:
    """
    res = []
    if 4 <= len(s) <= 12:
        dfs(s, '', res, 1)
    return res


def restoreIpAddresses2(s: str):
    """
    不使用递归，直接暴力搜索法
    :param s:
    :return:
    """
    result = list()
    for i in range(1, 4):
        w1 = s[:i]
        if not is_valid(w1):
            continue

        for j in range(i + 1, i + 4):
            w2 = s[i:j]
            if not is_valid(w2):
                continue

            for k in range(j + 1, j + 4):
                w3, w4 = s[j:k], s[k:]
                if not is_valid(w3) or not is_valid(w4):
                    continue

                result.append(w1 + '.' + w2 + '.' + w3 + '.' + w4)

    return result


if __name__ == '__main__':
    s = "222345"
    print(restoreIpAddresses(s))
    print(restoreIpAddresses2(s))
