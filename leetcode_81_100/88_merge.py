# -*- coding: utf-8 -*-
# @Time        : 2019/7/18 14:47
# @Author      : tianyunzqs
# @Description : 

"""
88. Merge Sorted Array
Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    依次将nums2中元素，插入nums1中
    从后往前遍历nums1，如果nums2中元素num小于nums1中元素，
    则将nums1中元素后移一个位置，直到遇到大于等于num的元素或者到nums1的头
    """
    for i, num in enumerate(nums2):
        j = 1
        while j <= m and num < nums1[m + i - j]:
            nums1[m + i - j + 1] = nums1[m + i - j]
            j += 1
        nums1[m + i - j + 1] = num


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
