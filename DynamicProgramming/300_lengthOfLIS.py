# -*- coding: utf-8 -*-
# @Time        : 2020/8/20 21:37
# @Author      : tianyunzqs
# @Description ：

"""
300. Longest Increasing Subsequence
Medium

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

from typing import List


class Solution:
    """
    dp[i]表示以nums[i]结尾的最长递增子序列
    dp[i]初始化为1是因为，只要nums不为空，则最长递增子序列最小等于1
    遍历到位置i时，嵌套一层从开始到位置i的遍历j，
    只要nums[i] > nums[j]，则dp[i] = max(dp[i], dp[j] + 1)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_len = len(nums)
        dp = [0 for _ in range(nums_len)]
        for i in range(nums_len):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    # print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
