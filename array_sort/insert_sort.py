# -*- coding: utf-8 -*-
# @Time        : 2019/7/15 11:13
# @Author      : tianyunzqs
# @Description : 


def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = tmp


if __name__ == '__main__':
    a = [2, 3, 2, 1, 7, 4, 0]
    insert_sort(a)
    print(a)
