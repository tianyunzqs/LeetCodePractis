# -*- coding: utf-8 -*-
# @Time        : 2020/5/5 17:02
# @Author      : tianyunzqs
# @Description : 

"""
据说著名犹太历史学家 Josephus 有过以下的故事：
在罗马人占领桥塔帕特后，39个犹太人与 Josephus 及他的朋友躲到一个洞中，
39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，
由第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新报数，
直到所有人都自杀身亡为止。然而 Josephus 和他的朋友并不想自杀，
问他俩安排的哪两个位置可以逃过这场死亡游戏？
————————————————
版权声明：本文为CSDN博主「HappyRocking」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/happyrocking/article/details/80058623
"""

import collections


def joseph_problem(a, b):
    # 将每个人依次编号，放入到队列中
    d = collections.deque(range(1, a+1))
    while d:
        d.rotate(-b)    # 队列向左旋转b步
        print(d.pop())  # 将最右边的删除，即自杀的人


if __name__ == '__main__':
    # 输出的是自杀的顺序。最后两个是16和31，说明这两个位置可以保证他俩的安全。
    joseph_problem(41, 3)
