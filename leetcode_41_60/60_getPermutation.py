# -*- coding: utf-8 -*-
# @Time        : 2019/6/30 12:45
# @Author      : tianyunzqs
# @Description ：

"""
60. Permutation Sequence
Medium


The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


def permuteUnique(nums):
    if len(nums) < 2:
        return [nums]
    if len(nums) == 2:
        if nums == nums[::-1]:
            return [nums]
        else:
            return [nums, nums[::-1]]

    a = permuteUnique(nums[1:])
    res = []
    for aa in a:
        for i in range(len(aa) + 1):
            tmp = aa[:i] + [nums[0]] + aa[i:]
            if tmp not in res:
                res.append(tmp)

    return res


def getPermutation(n, k):
    nums = list(range(1, n+1))
    res = permuteUnique(nums)
    print(res)
    res.sort()
    return ''.join([str(s) for s in res[k-1]]) if k <= len(res) else ''


if __name__ == '__main__':
    nums = [1, 2, 3]
    # print(permuteUnique(nums))
    print(getPermutation(8, 31492))
