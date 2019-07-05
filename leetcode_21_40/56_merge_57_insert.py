# -*- coding: utf-8 -*-
# @Time        : 2019/7/1 9:12
# @Author      : tianyunzqs
# @Description : 


def merge(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort()
    new_intervals = [intervals[0]]
    for interval in intervals[1:]:
        if new_intervals[-1][1] >= interval[0]:
            if new_intervals[-1][1] < interval[1]:
                new_intervals[-1][1] = interval[1]
        else:
            new_intervals.append(interval)

    return new_intervals


def insert(intervals, newInterval):
    intervals += [newInterval]
    return merge(intervals)


intervals = [[1,3],[2,6],[8,10],[15,18]]    # [[1,6],[8,10],[15,18]]
# intervals = [[1,3], [2,4],[4,5]]   # [[1,5]]
# intervals = [[1,4], [0,4]]
# intervals = [[1,4], [2,3]]
print(merge(intervals))


intervals = [[1,3],[6,9]]
newInterval = [2,5]
# [[1,5],[6,9]]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# [[1,2],[3,10],[12,16]]

print(insert(intervals, newInterval))
