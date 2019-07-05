# -*- coding: utf-8 -*-
# @Time        : 2019/6/18 18:04
# @Author      : tianyunzqs
# @Description : 

import copy
import itertools


def print_board(board):
    for i in range(9):
        print(board[i])


def isValidSudoku(board) -> bool:
    # 比较行是否合法
    for i in range(9):
        row = [int(item) for item in board[i] if item != '.']
        if len(row) != len(set(row)):
            return False
    # 比较列是否合法
    for i in range(9):
        col = [int(board[j][i]) for j in range(9) if board[j][i] != '.']
        if len(col) != len(set(col)):
            return False
    # 比较3*3单元格是否合法
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            box += board[i][j: j + 3]
            box += board[i + 1][j: j + 3]
            box += board[i + 2][j: j + 3]

            box = list(filter(lambda x: x != '.', box))
            if len(box) != len(set(box)):
                return False

    return True


def isVaildRow(board):
    # 比较行是否合法
    for i in range(9):
        row = set([list(item)[0] for item in board[i] if len(item) == 1])
        for j in range(9):
            if len(board[i][j]) != 1:
                board[i][j] &= set(range(1, 10)) - row
                if not board[i][j]:
                    return False
        row = [list(item)[0] for item in board[i] if len(item) == 1]
        if len(row) != len(set(row)):
            return False

    return True


def isVaildCol(board):
    # 比较列是否合法
    for i in range(9):
        col = set([list(board[j][i])[0] for j in range(9) if len(board[j][i]) == 1])
        for j in range(9):
            if len(board[j][i]) != 1:
                board[j][i] &= set(range(1, 10)) - col
                if not board[i][j]:
                    return False

        col = [list(board[j][i])[0] for j in range(9) if len(board[j][i]) == 1]
        if len(col) != len(set(col)):
            return False

    return True


def isVaildBox(board):
    # 比较3*3单元格是否合法
    for (i, j) in itertools.product(range(0, 9, 3), range(0, 9, 3)):
        box = []
        box += board[i][j: j + 3]
        box += board[i + 1][j: j + 3]
        box += board[i + 2][j: j + 3]

        box_cnt = {}
        for item in box:
            for it in item:
                if it not in box_cnt:
                    box_cnt[it] = 1
                else:
                    box_cnt[it] += 1
        one_cnt = [item[0] for item in filter(lambda x: x[1] == 1, box_cnt.items())]

        box = set([list(item)[0] for item in filter(lambda x: len(x) == 1, box)])
        for (m, n) in itertools.product(range(0, 3), range(0, 3)):
            if len(board[i + m][j + n]) != 1:
                board[i + m][j + n] &= set(range(1, 10)) - box
                if not board[i + m][j + n]:
                    return False
                for item in one_cnt:
                    if item in board[i + m][j + n]:
                        board[i + m][j + n] = {item}

        box = []
        box += board[i][j: j + 3]
        box += board[i + 1][j: j + 3]
        box += board[i + 2][j: j + 3]
        box = [list(item)[0] for item in filter(lambda x: len(x) == 1, box)]
        if len(box) != len(set(box)):
            return False

    return True


def empty_num(board):
    cnt = 0
    for i in range(9):
        for j in range(9):
            if len(board[i][j]) != 1:
                cnt += 1
    return cnt


def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    last_cnt = cnt = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                board[i][j] = {int(board[i][j])}
            else:
                board[i][j] = set(range(1, 10))
                cnt += 1

    board_bak = board
    idx, idy, idv, idv2 = -1, -1,  10, []
    flag = 0
    while cnt:
        if last_cnt == cnt:
            for (i, j) in itertools.product(range(9), range(9)):
                if len(board[i][j]) > 1:
                    board_bak = copy.deepcopy(board)
                    if flag == 0:
                        board_bak[i][j] = {list(board_bak[i][j])[0]}
                    else:
                        tmp = [v for v in board_bak[i][j] if v not in idv2]
                        if not tmp:
                            continue
                        board_bak[i][j] = {tmp[0]}
                        if i != idx or j != idy:
                            flag = 0
                            idv2 = []
                    idx, idy, idv = i, j, list(board_bak[i][j])[0]
                    idv2.append(list(board_bak[i][j])[0])
                    last_cnt = 0
                    break
            flag += 1
            continue

        if not isVaildRow(board_bak):
            board[idx][idy].remove(idv)
            last_cnt = cnt
            continue

        if not isVaildCol(board_bak):
            board[idx][idy].remove(idv)
            last_cnt = cnt
            continue

        if not isVaildBox(board_bak):
            board[idx][idy].remove(idv)
            last_cnt = cnt
            continue

        last_cnt = cnt
        cnt = empty_num(board_bak)

    for i in range(9):
        for j in range(9):
            board[i][j] = str(list(board_bak[i][j])[0])


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# board = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# board = [
#     [".",".","9","7","4","8",".",".","."],
#     ["7",".",".",".",".",".",".",".","."],
#     [".","2",".","1",".","9",".",".","."],
#     [".",".","7",".",".",".","2","4","."],
#     [".","6","4",".","1",".","5","9","."],
#     [".","9","8",".",".",".","3",".","."],
#     [".",".",".","8",".","3",".","2","."],
#     [".",".",".",".",".",".",".",".","6"],
#     [".",".",".","2","7","5","9",".","."]
# ]
# board = [
#     [".",".",".","2",".",".",".","6","3"],
#     ["3",".",".",".",".","5","4",".","1"],
#     [".",".","1",".",".","3","9","8","."],
#     [".",".",".",".",".",".",".","9","."],
#     [".",".",".","5","3","8",".",".","."],
#     [".","3",".",".",".",".",".",".","."],
#     [".","2","6","3",".",".","5",".","."],
#     ["5",".","3","7",".",".",".",".","8"],
#     ["4","7",".",".",".","1",".",".","."]
# ]
# board = [
#     [".",".",".","2",".",".",".","6","3"],
#     ["3",".",".",".",".","5","4",".","1"],
#     [".",".","1",".",".","3","9","8","."],
#     [".",".",".",".",".",".",".","9","."],
#     [".",".",".","5","3","8",".",".","."],
#     [".","3",".",".",".",".",".",".","."],
#     [".","2","6","3",".",".","5",".","."],
#     ["5",".","3","7",".",".",".",".","8"],
#     ["4","7",".",".",".","1",".",".","."]
# ]
board = [
    [".",".",".",".",".","7",".",".","9"],
    [".","4",".",".","8","1","2",".","."],
    [".",".",".","9",".",".",".","1","."],
    [".",".","5","3",".",".",".","7","2"],
    ["2","9","3",".",".",".",".","5","."],
    [".",".",".",".",".","5","3",".","."],
    ["8",".",".",".","2","3",".",".","."],
    ["7",".",".",".","5",".",".","4","."],
    ["5","3","1",".","7",".",".",".","."]
]

# print(isValidSudoku(board))
solveSudoku(board)
print_board(board)
