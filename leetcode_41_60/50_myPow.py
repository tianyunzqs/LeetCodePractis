# -*- coding: utf-8 -*-
# @Time        : 2019/6/27 17:45
# @Author      : tianyunzqs
# @Description : 


def myPow(x, n):
    """
    二分法递归方式
    :param x:
    :param n:
    :return:
    """

    def fun(y, n):
        if n == 0:
            return 1.0
        if n == 1:
            return y
        if n % 2:
            res = fun(y, n // 2)
            return res * res * y
        else:
            res = fun(y, n // 2)
            return res * res

    if n > 0:
        if x > 0:
            return fun(x, n)
        else:
            x = abs(x)
            if n % 2 == 0:
                return fun(x, n)
            else:
                return -1.0 * fun(x, n)
    else:
        n = abs(n)
        if x > 0:
            return 1.0 / fun(x, n)
        else:
            x = abs(x)
            if n % 2 == 0:
                return 1.0 / fun(x, n)
            else:
                return -1.0 / fun(x, n)


x = -2.00000
n = -3
print(myPow(x, n))
