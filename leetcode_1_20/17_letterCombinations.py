# -*- coding: utf-8 -*-
# @Time        : 2019/6/11 9:33
# @Author      : tianyunzqs
# @Description : 


def letterCombinations(digits):
    digits2letter = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def combine(_list1, _list2):
        if not _list1 or not _list2:
            return _list1 or _list2

        combine_result = set()
        for l1 in _list1:
            for l2 in _list2:
                combine_result.add(l1 + l2)
        return list(combine_result)

    result = []
    for digit in digits:
        result = combine(result, digits2letter[digit])

    return result


d = '23'
print(letterCombinations(d))
