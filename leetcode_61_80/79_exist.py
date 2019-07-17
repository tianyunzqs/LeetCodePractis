# -*- coding: utf-8 -*-
# @Time        : 2019/7/15 17:39
# @Author      : tianyunzqs
# @Description : 

"""
79. Word Search
Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


def find(board, word, i, j, m, n):
    """
    从i,j开始深度优先搜索word是否在board中
    如果在递归中修改了可变对象的值，在递归函数结束之后要改回来
    :param board:
    :param word:
    :param i:
    :param j:
    :param m:
    :param n:
    :return:
    """
    if not word:
        return True
    if i < 0 or i >= m or j < 0 or j >= n:
        return False
    elif word[0] == board[i][j]:
        board[i][j] = None  # 标记
        res = find(board, word[1:], i + 1, j, m, n) or \
              find(board, word[1:], i - 1, j, m, n) or \
              find(board, word[1:], i, j + 1, m, n) or \
              find(board, word[1:], i, j - 1, m, n)
        board[i][j] = word[0]  # 恢复原来的值

        return res


def exist(board: list, word: str) -> bool:
    if not word:
        return True
    if not board or not board[0]:
        return False

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if find(board, word, i, j, m, n):
                return True
    else:
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "AAA"
    print(exist(board, word))
