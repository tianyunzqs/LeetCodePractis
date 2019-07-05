# -*- coding: utf-8 -*-
# @Time        : 2019/6/18 17:11
# @Author      : tianyunzqs
# @Description : 


def searchInsert(nums, target: int) -> int:
    # # solution1
    # try:
    #     return nums.index(target)
    # except:
    #     nums = nums + [target]
    #     nums.sort()
    #     return nums.index(target)

    # solution2
    if not nums or target <= nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)

    i = 0
    while i < len(nums) - 1:
        if nums[i] == target:
            return i
        if nums[i] < target <= nums[i + 1]:
            return i + 1
        i += 1


nums = [1,3]
target = 3
print(searchInsert(nums, target))
