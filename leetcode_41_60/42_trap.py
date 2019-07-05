# -*- coding: utf-8 -*-
# @Time        : 2019/6/25 9:25
# @Author      : tianyunzqs
# @Description : 


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


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
# height = [3, 2, 1]
height = [3, 2, 1, 0, 1, 2]
print(trap(height))
