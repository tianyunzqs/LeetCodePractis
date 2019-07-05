# -*- coding: utf-8 -*-
# @Time        : 2019/6/20 18:56
# @Author      : tianyunzqs
# @Description :


def combinationSum3(candidates, target):
    candidates.sort()
    res = []

    def fun(candidates, target, result):
        for candidate in candidates:
            # 比较target与candidate值的大小
            if target - candidate == 0:   # 相等，说明已找到一组值相加等于target
                result.append(candidate)
                res.append(result)
                return
            elif target - candidate < 0:  # 如果target小于candidate，说明无相加等于target的子组
                return
            else:  # 如果target大于candidate，说明还可以继续对target进行分解，继续递归
                fun(candidates, target - candidate, result + [candidate])

    fun(candidates, target, [])
    return [list(r) for r in set([tuple(sorted(item)) for item in res])]


def combinationSum2(candidates, target):
    candidates.sort()
    ans = []

    def helper(sums, path):
        for n in candidates:
            if not path or n >= path[-1]:
                if sums + n == target:
                    ans.append(path + [n])
                    return
                elif sums + n < target:
                    helper(sums + n, path + [n])
                else:
                    return

    helper(0, [])
    return ans


candidates = [2,3,6,7]
target = 7
candidates = [2,3,5]
target = 9

# candidates = [1,2]
# target = 4
candidates = [8,7,4,3]
target = 11

result = combinationSum3(candidates, target)
print(result)
