# -*- coding: utf-8 -*-
# @Time        : 2019/6/27 10:39
# @Author      : tianyunzqs
# @Description : 


def groupAnagrams(strs):
    result = dict()
    for s in strs:
        s_sorted = ''.join(sorted(s))
        if s_sorted not in result:
            result[s_sorted] = [s]
        else:
            result[s_sorted].append(s)

    return list(result.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
