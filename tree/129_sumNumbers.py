# -*- coding: utf-8 -*-
# @Time        : 2021/6/4 14:36
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
129. 求根节点到叶节点数字之和
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。


示例 1：
输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25

示例 2：
输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026


提示：
树中节点的数目在范围 [1, 1000] 内
0 <= Node.val <= 9
树的深度不超过 10
"""

import uuid
from random import sample
from typing import List
from graphviz import Digraph


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def build_tree(nums, cnt=[0]):
    """
    创建二叉树
    :param nums: 根据前序遍历整理的数组，空节点用None表示，叶子节点的左右节点都是None
    :param cnt: 计数器
    :return:
    """
    if not nums:
        return None

    x = nums[cnt[0]]
    cnt[0] += 1
    if x is None:
        bt = None
    else:
        bt = TreeNode(x)
        bt.left = build_tree(nums, cnt)
        bt.right = build_tree(nums, cnt)

    return bt


def print_tree_preorder(root: TreeNode):
    """
    前序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []

    def preoder(root):
        if root:
            res.append(root.val)
            preoder(root.left)
            preoder(root.right)
        else:
            res.append(None)

    preoder(root)
    return res


def print_tree_inorder(root: TreeNode):
    """
    中序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []

    def inoder(root):
        if root:
            inoder(root.left)
            res.append(root.val)
            inoder(root.right)
        else:
            res.append(None)

    inoder(root)
    return res


def print_tree_postorder(root: TreeNode):
    """
    后序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []

    def postoder(root):
        if root:
            postoder(root.left)
            postoder(root.right)
            res.append(root.val)
        else:
            res.append(None)

    postoder(root)
    return res


def print_tree_levelorder1(root: TreeNode):
    """
    层序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []
    if not root:
        return []
    queue = [root]
    while len(queue) > 0:  # 直到队列中节点全部被取出
        node = queue.pop(0)   # 先入对列先出（模拟队列）
        res.append(node.val)
        # 左右孩子节点都入列队，出队列的时候，按先进先出原则
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


def print_tree_levelorder(root: TreeNode):
    """
    层序遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []
    if not root:
        return []
    queue = [root]
    while len(queue) > 0:  # 直到队列中节点全部被取出
        tmp = []
        level_size = len(queue)
        for i in range(level_size):  # 队列中保存的是每一层的节点
            node = queue.pop(0)   # 先入对列先出（模拟队列）
            tmp.append(node.val)
            # 左右孩子节点都入列队，出队列的时候，按先进先出原则
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    return res


def print_tree_deeporder(root: TreeNode):
    """
    深度优先遍历
    :param root: 二叉树的根节点
    :return:
    """
    res = []
    if not root:
        return []
    queue = [root]
    while len(queue) > 0:
        node = queue.pop()
        res.append(node.val)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return res


def print_tree_height(root: TreeNode):
    """
    二叉树的高度
    :param root:
    :return:
    """
    if not root:
        return 0
    left_height = print_tree_height(root.left)
    right_height = print_tree_height(root.right)
    return left_height + 1 if left_height > right_height else right_height + 1


def print_all_path(root: TreeNode):
    """
    二叉树所有路径
    :param root:
    :return:
    """
    def all_path(root, paths=[]):
        if not root:
            return
        paths.append(root.val)
        if not root.left and not root.right:
            all_paths.append(paths[:])
        if root.left:
            all_path(root.left, paths)
        if root.right:
            all_path(root.right, paths)
        paths.pop()

    all_paths = []
    all_path(root)
    return all_paths


# 利用Graphviz实现二叉树的可视化
def view_tree(root, save_path='Binary_Tree.gv', label=False):
    dot = Digraph(comment='Binary Tree')
    # colors for labels of nodes
    colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']

    # 绘制以某个节点为根节点的二叉树
    def print_node(node, node_tag):
        # 节点颜色
        color = sample(colors, 1)[0]
        if node.left is not None:
            left_tag = str(uuid.uuid1())            # 左节点的数据
            dot.node(left_tag, str(node.left.val), style='filled', color=color)    # 左节点
            label_string = 'L' if label else ''    # 是否在连接线上写上标签，表明为左子树
            dot.edge(node_tag, left_tag, label=label_string)   # 左节点与其父节点的连线
            print_node(node.left, left_tag)

        if node.right is not None:
            right_tag = str(uuid.uuid1())
            dot.node(right_tag, str(node.right.val), style='filled', color=color)
            label_string = 'R' if label else ''  # 是否在连接线上写上标签，表明为右子树
            dot.edge(node_tag, right_tag, label=label_string)
            print_node(node.right, right_tag)

    # 如果树非空
    if root.val is not None:
        root_tag = str(uuid.uuid1())                # 根节点标签
        dot.node(root_tag, str(root.val), style='filled', color=sample(colors, 1)[0])     # 创建根节点
        print_node(root, root_tag)

    dot.render(save_path)
    # dot.view(save_path)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def all_path(root, paths=[]):
            global total
            if not root:
                return
            paths.append(root.val)
            if not root.left and not root.right:
                # all_paths.append(paths[:])
                total += int(''.join([str(s) for s in paths[:]]))
            if root.left:
                all_path(root.left, paths)
            if root.right:
                all_path(root.right, paths)
            paths.pop()

        global total
        total = 0
        all_paths = []
        all_path(root)
        return total


if __name__ == '__main__':
    nums = [3, 9, None, None, 20, 17, None, None, 7, None, None]
    nums = [1, 2, 3, 4, None, None, 4, None, None, 3, None, None, 2, None, None]
    nums = [1, 2, 3, None, 4, None, None, None, 2, 3, None, None, 4, None, None]
    # nums = [5, 4, 3, 7, None, None, 2, None, None, None, 8, 0, None, None, 4, 5, None, None, 1, None, None]
    # nums = [1, 2, None, None, 3, None, None]
    # nums = [1, 2, None, None, None]
    tree_root = build_tree(nums, [0])
    print(print_tree_levelorder(tree_root))
    print(print_tree_deeporder(tree_root))
    print(Solution().sumNumbers(tree_root))
