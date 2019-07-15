# -*- coding: utf-8 -*-
# @Time        : 2019/7/15 10:52
# @Author      : tianyunzqs
# @Description : 


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        flag = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True

        if not flag:
            break


if __name__ == '__main__':
    a = [2, 3, 1, 7, 4, 0]
    bubble_sort(a)
    print(a)
