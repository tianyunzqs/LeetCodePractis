# -*- coding: utf-8 -*-
# @Time        : 2019/7/9 11:01
# @Author      : tianyunzqs
# @Description : 

"""
75. Sort Colors
Medium

Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


def sortColors1(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    solution1：内置排序函数
    """
    nums.sort()


def sortColors2(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    solution2：题目中提示的解法，空间复杂度O(n)，时间复杂度O(n)
    先统计数组中0,1,2的个数，然后依次替换原数组中数字即可
    """
    if not nums:
        return nums

    nums_cnt = {}
    for num in nums:
        if num not in nums_cnt:
            nums_cnt[num] = 1
        else:
            nums_cnt[num] += 1

    start, end = 0, 0
    for i in range(3):
        end = start + nums_cnt[i]
        nums[start: end] = [i] * nums_cnt[i]
        start = end


def sortColors3(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    solution3：快速排序，时间复杂度O(logN)，空间复杂度O(1)
    快排基本思想：
    在待排序的n个记录中任取一个记录（通常取第一个记录），
    以该记录为基准，将当前的无序区划分为左右两个较小的无
    序子区，使左边的记录均小于基准值，右边的记录均大于或
    等于基准值，基准值位于两个无序区的中间位置（即该记录
    最终的排序位置）。之后，分别对两个无序区进行上述的划
    分过程，直到无序区所有记录都排序完毕。
    """
    def partition(nums, low, high):
        key_prov = nums[low]
        while low < high:
            while low < high and nums[high] >= key_prov:
                high -= 1
            nums[low], nums[high] = nums[high], nums[low]

            while low < high and nums[low] <= key_prov:
                low += 1
            nums[low], nums[high] = nums[high], nums[low]
        return low

    def quick_sort(nums, low, high):
        if low < high:
            prov = partition(nums, low, high)
            quick_sort(nums, low, prov-1)
            quick_sort(nums, prov+1, high)

    quick_sort(nums, 0, len(nums)-1)


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    # nums = []
    # sortColors1(nums)
    # sortColors2(nums)
    sortColors3(nums)
    print(nums)
