# -*- coding: utf-8 -*-
# @Time        : 2019/6/28 17:54
# @Author      : tianyunzqs
# @Description :

"""
53. Maximum Subarray
Easy


Given an integer array nums,
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
"""


def maxSubArray(nums):
    """
    遍历数组，逐步累加得到local_total，
    如果local_total > 0，则继续累加，否则将local_total清零
    如果local_total <= 0，则说明继续累加会降低最大值，故重新开始
    取最终最大值为max(local_num+num, global_max)
    :param nums:
    :return:
    """
    local_total, global_max = 0, sum(nums)
    for num in nums:
        global_max = max(global_max, local_total + num)
        local_total = max(0, local_total + num)
    return global_max


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
