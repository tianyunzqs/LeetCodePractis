# -*- coding: utf-8 -*-
# @Time        : 2019/7/17 18:05
# @Author      : tianyunzqs
# @Description : 

"""
84. Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10
"""


def largestRectangleArea2(heights) -> int:
    """
    错误
    :param heights:
    :return:
    """
    if not heights:
        return 0
    if len(heights) <= 2:
        if all(heights):
            return min(heights) * len(heights)
        else:
            return max(heights)

    left, right = 0, len(heights) - 1
    max_area = min(heights) * len(heights)
    while left < right:
        letf_area = min(heights[left: right]) * (right - left)
        right_area = min(heights[left+1: right+1]) * (right - left)
        if letf_area > right_area:
            right -= 1
            max_area = max(max_area, letf_area)
        else:
            left += 1
            max_area = max(max_area, right_area)

    return max_area


def largestRectangleArea(height):
    """
    直方图矩形面积要最大的话，需要尽可能的使得连续的矩形多，并且最低一块的高度要高。
    有点像木桶原理一样，总是最低的那块板子决定桶的装水量。
    那么既然需要用单调栈来做，首先要考虑到底用递增栈，还是用递减栈来做。
    我们想啊，递增栈是维护递增的顺序，
    当遇到小于栈顶元素的数就开始处理，而递减栈正好相反，维护递减的顺序，
    当遇到大于栈顶元素的数开始处理。
    那么根据这道题的特点，我们需要按从高板子到低板子的顺序处理，先处理最高的板子，宽度为1，
    然后再处理旁边矮一些的板子，此时长度为2，因为之前的高板子可组成矮板子的矩形，
    因此我们需要一个递增栈，当遇到大的数字直接进栈，
    而当遇到小于栈顶元素的数字时，就要取出栈顶元素进行处理了，那取出的顺序就是从高板子到矮板子了，
    于是乎遇到的较小的数字只是一个触发，表示现在需要开始计算矩形面积了，
    为了使得最后一块板子也被处理，这里用了个小 trick，在高度数组最后面加上一个0，这样原先的最后一个板子也可以被处理了。
    由于栈顶元素是矩形的高度，那么关键就是求出来宽度，
    那么跟之前那道 Trapping Rain Water 一样，单调栈中不能放高度，而是需要放坐标。
    由于我们先取出栈中最高的板子，那么就可以先算出长度为1的矩形面积了，
    然后再取下一个板子，此时根据矮板子的高度算长度为2的矩形面积，
    以此类推，知道数字大于栈顶元素为止，再次进栈，巧妙的一比！
    关于单调栈问题可以参见博主的一篇总结帖 LeetCode Monotonous Stack Summary 单调栈小结
    :param height:
    :return:
    """
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans


if __name__ == '__main__':
    nums = [2,1,5,6,2,3]
    # nums = [1, 2, 2]
    print(largestRectangleArea(nums))
