# -*- coding: utf-8 -*-
# @Time        : 2019/7/17 9:44
# @Author      : tianyunzqs
# @Description : 

"""
80. Remove Duplicates from Sorted Array II
Medium

Given a sorted array nums, remove the duplicates in-place
such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7,
with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference,
which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


def removeDuplicates(nums) -> int:
    """
    定义一个变量保存数组中元素，
    同时定义一个变量保存该元素出现的次数。
    如果次数大于2，则删除该元素一次，同时次数减一
    :param nums:
    :return:
    """
    if not nums:
        return 0

    i = 1
    element, count = nums[0], 1
    while True:
        if i >= len(nums):
            break
        if nums[i] == element:
            count += 1
            if count > 2:
                nums.remove(element)
                count -= 1
            else:
                i += 1
        else:
            element, count = nums[i], 1
            i += 1
    return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums = [0,0,1,1,1,1,2,3,3]
    length = removeDuplicates(nums)
    print(nums)
    print(length)
