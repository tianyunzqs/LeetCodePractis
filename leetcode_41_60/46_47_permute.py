# -*- coding: utf-8 -*-
# @Time        : 2019/6/26 17:20
# @Author      : tianyunzqs
# @Description : 


def permute(nums):

    def fun(nums2):
        if len(nums2) == 2:
            return [nums2, nums2[::-1]]

        a = fun(nums2[1:])
        res = []
        for aa in a:
            for i in range(len(aa) + 1):
                tmp = aa[:i] + [nums2[0]] + aa[i:]
                if tmp not in res:
                    res.append(tmp)
        return res

    if len(nums) < 2:
        return [nums]
    else:
        return fun(nums)


def permute2(nums):
    if len(nums) < 2:
        return [nums]
    if len(nums) == 2:
        if nums == nums[::-1]:
            return [nums]
        else:
            return [nums, nums[::-1]]

    a = permute2(nums[1:])
    res = []
    for aa in a:
        for i in range(len(aa) + 1):
            tmp = aa[:i] + [nums[0]] + aa[i:]
            if tmp not in res:
                res.append(tmp)
    return res


def getPermutation(n: int, k: int) -> str:
    """
    使用递归求出所有排列后，再取第k个，这样会超时
    由于只要求求出第k个排列，因此只需定位即可，不用全部求出
    :param n:
    :param k:
    :return:
    """
    def factorial(x):
        fac = 1
        for i in range(2, x+1):
            fac *= i
        return fac
    candidate = [i for i in range(1, n+1)]
    val = []
    k -= 1  # 转换为数组下标
    for i in range(1, n+1):
        idx = k // factorial(n-i)
        val.append(candidate[idx])
        candidate.pop(idx)
        k = k % factorial(n-i)

    return ''.join([str(s) for s in val])


# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# result = permute2(nums)
# for i in result:
#     print(i)
# print(len(result))


import itertools

for i in itertools.permutations([1, 2, 3, 4]):
    print(i)


print(getPermutation(4, 16))