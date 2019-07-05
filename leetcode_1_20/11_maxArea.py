# -*- coding: utf-8 -*-
# @Time        : 2019/4/15 11:27
# @Author      : tianyunzqs
# @Description : 


def maxArea( height) -> int:
    i, j = 0, len(height) - 1
    max_area = 0
    while i < j:
        area = (j - i) * min(height[i], height[j])
        if area > max_area:
            max_area = area
        else:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
    return max_area


    # max_area = 0
    # for i, v in enumerate(height):
    #     x = max([abs(i - ii) for ii, vv in enumerate(height) if vv >= v])
    #     max_area = max(max_area, x * v)
    # return max_area


if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))
