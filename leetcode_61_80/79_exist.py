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


def exist(board: list, word: str) -> bool:
    if not word:
        return True
    if not board or not board[0]:
        return False

    m, n = len(board), len(board[0])
    dp = [[False for _ in range(n)] for _ in range(m)]
    dp[0][0] = True if len(word) == 1 and word == board[0][0] else False
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] and


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(exist(board, word))
