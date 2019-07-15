# -*- coding: utf-8 -*-
# @Time        : 2019/7/15 11:45
# @Author      : tianyunzqs
# @Description : 


def partition(nums, low, high):
    prov = nums[low]
    while low < high:
        while low < high and nums[high] >= prov:
            high -= 1
        nums[low], nums[high] = nums[high], nums[low]
        while low < high and nums[low] <= prov:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]

    return low


def quick(nums, low, high):
    if low < high:
        prov = partition(nums, low, high)
        quick(nums, low, prov-1)
        quick(nums, prov+1, high)


def quick_sort(nums):
    quick(nums, 0, len(nums)-1)


if __name__ == '__main__':
    a = [2, 3, 2, 1, 7, 4, 0]
    quick_sort(a)
    print(a)
