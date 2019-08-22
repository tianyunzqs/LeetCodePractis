# -*- coding: utf-8 -*-
# @Time        : 2019/7/19 14:22
# @Author      : tianyunzqs
# @Description : 

"""
94. Binary Tree Inorder Traversal
Medium

Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
        bt.left = build_tree(nums)
        bt.right = build_tree(nums)

    return bt


def print_tree(root: TreeNode):
    """
    以前序遍历方式输出
    :param root: 二叉树的根节点
    :return:
    """
    if root:
        print(root.val, end='->')
        print_tree(root.left)
        print_tree(root.right)
    else:
        print(None, end='->')


def inorderTraversal(root: TreeNode):
    res = []

    def inorder(root):
        if root:
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

    inorder(root)
    return res


if __name__ == '__main__':
    a = [1, None, 2, 3, None, None, None]
    # a = []
    root = build_tree(a)
    print_tree(root)
    print(inorderTraversal(root))
