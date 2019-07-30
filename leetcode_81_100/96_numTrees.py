# -*- coding: utf-8 -*-
# @Time        : 2019/7/26 17:24
# @Author      : tianyunzqs
# @Description : 

"""
96. Unique Binary Search Trees
Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


def numTrees(n: int) -> int:
    """
    典型的卡特兰数问题
    令h(1)=1，Catalan数满足递归式：
    h(n) = h(1)h(n-1) + h(2) h(n-2) + … + h(n-1)*h(1)，n>=2

    该递推关系的解为：h(n) = C(2n, n)/(n+1) = C(2n, n) - C(2n, n-1)
    :param n:
    :return:
    """
    if n <= 0:
        return 0

    res = [0 for _ in range(n+1)]
    res[0] = 1
    res[1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            res[i] += res[j-1] * res[i-j]

    return res[-1]


if __name__ == '__main__':
    print(numTrees(19))
