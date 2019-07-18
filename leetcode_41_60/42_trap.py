# -*- coding: utf-8 -*-
# @Time        : 2019/6/25 9:25
# @Author      : tianyunzqs
# @Description : 

"""
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


def trap(height):
    """
    定义两个指针left和right，分别从前往后和从后往前遍历，直至相遇。
    当从前往后遍历的时候，找到当前位置前面的最大值，减去当前位置高度，即为当前可存储的雨水容量，将其累加到总量中；
    当从后往前遍历的时候，找到当前位置后面的最大值，减去当前位置高度，即为当前可存储的雨水容量，将其累加到总量中。
    PS：最大值减去当前位置高度即为雨水量的前提是保证从前往后的最大值一定要小于等于从后往前的最大值，也即可以兜住雨水。
    :param height:
    :return:
    """
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left <= right:
        if left_max <= right_max:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1

    return water


def trap2(height):
    """
    栈
    :param height:
    :return:
    """
    st = []
    i, n = 0, len(height)
    res = 0
    while i < n:
        if not st or height[i] <= height[st[-1]]:
            st.append(i)
            i += 1
        else:
            t = st[-1]
            st.pop()
            if not st:
                continue
            h = min(height[i], height[st[-1]]) - height[t]
            w = i - st[-1] - 1
            res += h * w
    return res


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
    # height = [3, 2, 1]
    # height = [3, 2, 1, 0, 1, 2]
    print(trap2(height))
    print(trap3(height))
