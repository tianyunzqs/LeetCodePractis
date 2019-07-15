# -*- coding: utf-8 -*-
# @Time        : 2019/7/15 13:55
# @Author      : tianyunzqs
# @Description : 


def select_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    a = [2, 3, 1, 7, 4, 0]
    select_sort(a)
    print(a)