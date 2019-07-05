# -*- coding: utf-8 -*-
# @Time        : 2019/6/17 11:45
# @Author      : tianyunzqs
# @Description : 


def nextPermutation2(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if sorted(nums, reverse=True) == nums:
        nums.sort()
        return
    if len(nums) < 3:
        nums.sort(reverse=True)
        return

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp

                nums[i + 1:] = sorted(nums[i + 1:])
                return


def nextPermutation(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    # find non - descending series(ascending series)
    while i > 0:
        if nums[i] > nums[i - 1]:
            break
        i -= 1

    # reverse(let this sub - sequence from descending to ascending)
    nums[i:] = sorted(nums[i:])

    # So-far, we can make sure this sub-sequence is ascending.But this sequence
    # is always lower than previous(1132->1123, 132->123)
    # This sub-sequence always fewer or equal to the origin.
    # So, we must find the second minimum(except the original) sub - sequence.
    if i == 0:
        return
    for s in range(i, len(nums)):
        if nums[s] > nums[i - 1]:
            tmp = nums[i - 1]
            nums[i - 1] = nums[s]
            nums[s] = tmp
            break


a = [4,2,0,2,3,2,1]
# a = [1,3,2]
nextPermutation(a)
print(a)
