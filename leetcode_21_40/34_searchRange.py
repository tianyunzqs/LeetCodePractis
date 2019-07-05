# -*- coding: utf-8 -*-
# @Time        : 2019/6/18 16:45
# @Author      : tianyunzqs
# @Description : 


def searchRange(nums, target: int):
    if not nums or target < nums[0] or target > nums[-1]:
        return [-1, -1]

    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] < target:
            left += 1
        if nums[right] > target:
            right -= 1
        if nums[left] == target and nums[right] == target:
            return [left, right]

    return [-1, -1]


nums = [1]
target = 1
print(searchRange(nums, target))
