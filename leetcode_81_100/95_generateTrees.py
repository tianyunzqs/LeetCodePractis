# -*- coding: utf-8 -*-
# @Time        : 2019/7/19 17:19
# @Author      : tianyunzqs
# @Description : 

"""
95. Unique Binary Search Trees II
Medium

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
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
    if not x:
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


def insert_node_to_bst(root: TreeNode, val):
    """
    向二叉排序树（二叉查找树、二叉搜索树）中插入节点
    :param root: 二叉排序树根节点
    :param val: 待插入节点值
    :return: 新的二叉排序树
    """
    if not root:  # 二叉排序树为空，直接将新结点赋值给根结点
        # 初始化新插入的结点
        new_node = TreeNode(val)
        new_node.left = None
        new_node.right = None
        root = new_node
    else:  # 如果二叉排序树不为空
        if root.val >= val:  # 需要在父结点的左边插入新结点
            root.left = insert_node_to_bst(root.left, val)
        else:                # 需要在父结点的右边插入新结点
            root.right = insert_node_to_bst(root.right, val)

    return root


def dfs(start, end):
    if start == end:
        return None
    result = []
    for i in range(start, end):
        for l in dfs(start, i) or [None]:
            for r in dfs(i + 1, end) or [None]:
                node = TreeNode(i)
                node.left, node.right = l, r
                result.append(node)
    return result


def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    if n == 0:
        return [[]]
    return dfs(1, n + 1)


if __name__ == '__main__':
    new_root = generateTrees(3)
    print_tree(new_root)
