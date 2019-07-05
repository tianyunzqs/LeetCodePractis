# -*- coding: utf-8 -*-
# @Time        : 2019/6/18 17:16
# @Author      : tianyunzqs
# @Description : 


def search(nums, target: int) -> int:
    # # solution1
    # try:
    #     return nums.index(target)
    # except:
    #     return -1

    # solution2
    if not nums:
        return -1
    if target <= nums[-1]:
        for i in range(len(nums) - 1, -1, -1):
            if target == nums[i]:
                return i
    else:
        for i in range(len(nums) - 1):
            if target == nums[i]:
                return i

    return -1


nums = [3,1]
target = 3
print(search(nums, target))
