# -*- coding: utf-8 -*-
# @Time        : 2019/6/28 17:54
# @Author      : tianyunzqs
# @Description :


def maxSubArray(nums) -> int:
    total = sum(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        if sum(nums[left+1:]) > total:
            left += 1
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1


    return total


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
