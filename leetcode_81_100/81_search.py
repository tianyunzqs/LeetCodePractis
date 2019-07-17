# -*- coding: utf-8 -*-
# @Time        : 2019/7/17 17:10
# @Author      : tianyunzqs
# @Description : 

"""
81. Search in Rotated Sorted Array II
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


def search(nums, target: int) -> bool:
    """
    解题思路跟33题一样，先判断target是在前半部分搜索还是后半部分搜索
    然后遍历即可
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return False

    if target <= nums[-1]:
        for i in range(len(nums) - 1, -1, -1):
            if target == nums[i]:
                return True
    else:
        for i in range(len(nums) - 1):
            if target == nums[i]:
                return True

    return False


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(search(nums, target))
