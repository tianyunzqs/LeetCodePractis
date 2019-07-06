# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 15:29
# @Author      : tianyunzqs
# @Description ：

"""
4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


def findMedianSortedArrays(nums1, nums2) -> float:
    nums = sorted(nums1 + nums2)
    if len(nums) % 2:
        return nums[len(nums) // 2]
    else:
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays(nums1, nums2))
