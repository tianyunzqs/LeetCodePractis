# -*- coding: utf-8 -*-
# @Time        : 2019/6/28 11:11
# @Author      : tianyunzqs
# @Description : 


class NQueueRecursion1D(object):
    def __init__(self):
        self.N = 20    # 最多放皇后的个数
        self.q = [0 for _ in range(self.N)]  # q[i]表示皇后所在的列号，i表示皇后所在的行号
        self.cont = 0  # 统计解的个数
        self.all_solve = []

    def save_solve(self, n):
        self.cont += 1
        one_solve = []
        for i in range(1, n + 1):
            one_row = ''
            for j in range(1, n + 1):
                if self.q[i] != j:
                    one_row += '.'
                else:
                    one_row += 'Q'
            one_solve.append(one_row)
        self.all_solve.append(one_solve)

    def print_solve(self, n):
        self.cont += 1
        print('第{0}个解'.format(self.cont))
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if self.q[i] != j:
                    print('. ', end='')
                else:
                    print('Q ', end='')
            print()
        print()

    def is_valid(self, i, k):
        """
        检验第i行的k列上是否可以摆放皇后
        :param i:
        :param k:
        :return:
        """
        for j in range(1, i):
            # 第j行的皇后是否在k列或(j,q[j])与(i,k)是否在斜线上
            if self.q[j] == k or abs(j - i) == abs(self.q[j] - k):
                return False
        return True

    def place(self, k, n):
        """
        放置皇后到棋盘上
        :param k:
        :param n:
        :return:
        """
        if k > n:
            self.save_solve(n)  # 递归出口
        else:
            # 试探第k行的每一个列
            for j in range(1, n + 1):
                if self.is_valid(k, j):
                    self.q[k] = j         # 保存位置
                    self.place(k + 1, n)  # 接着试探下一行


class NQueueRecursion2D(object):
    def __init__(self, n):
        pass

    def save_solve(self):
        self.cont += 1
        one_solve = []
        for row_q in self.q:
            one_solve.append(''.join(row_q))
        self.all_solve.append(one_solve)

    def print_solve(self):
        self.cont += 1
        print('第{0}个解'.format(self.cont))
        for row_q in self.q:
            print(''.join(row_q))
        print()

    def is_valid(self, x, y, n):
        """
        检验第x行的y列上是否可以摆放皇后
        :param x:
        :param y:
        :return:
        """
        if 'Q' in self.q[x]:
            return False

        for i in range(n):
            if self.q[i][y] == 'Q':
                return False
            if 0 <= i+x-y < n and self.q[i+x-y][i] == 'Q':   # 右斜角线
                return False
            if 0 <= x+y-i < n and self.q[x+y-i][i] == 'Q':   # 左斜角线
                return False
        return True

    def place(self, k, n):
        """
        放置皇后到棋盘上
        :param k:
        :param n:
        :return:
        """
        if k >= n:
            self.save_solve()  # 递归出口
        else:
            # 试探第k行的每一个列
            for j in range(n):
                if self.is_valid(k, j, n):
                    self.q[k][j] = 'Q'         # 保存位置
                    self.place(k + 1, n)  # 接着试探下一行
                    self.q[k][j] = '.'    # 不满足条件，则清除上一步已放置的皇后

    def solveNQueens(self, n):
        self.q = [['.' for _ in range(n)] for _ in range(n)]
        self.cont = 0  # 统计解的个数
        self.all_solve = []
        self.place(0, n)


n = 8
nq1d = NQueueRecursion2D(n)
nq1d.place(0, n)
