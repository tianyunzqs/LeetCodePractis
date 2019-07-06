# -*- coding: utf-8 -*-
# @Time        : 2019/7/1 10:18
# @Author      : tianyunzqs
# @Description : 


def lengthOfLastWord(s):
    s = s.strip()
    return len(s.split(' ')[-1]) if s else 0


s = 'HelloWorld'
print(lengthOfLastWord(s))
