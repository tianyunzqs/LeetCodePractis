# -*- coding: utf-8 -*-
# @Time        : 2019/8/11 9:45
# @Author      : tianyunzqs
# @Description ：

"""
98. Validate Binary Search Tree
Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
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


def isValidBST(root: TreeNode) -> bool:
    if not root:
        return True

    if root.left and root.right:
        if root.left.val < root.val < root.right.val:
            return isValidBST(root.left) and isValidBST(root.right)
        else:
            return False

    elif root.left:
        if root.left.val < root.val:
            return isValidBST(root.left)
        else:
            return False
    elif root.right:
        if root.right.val > root.val:
            return isValidBST(root.right)
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    # nums = [5, 1, 4, None, None, 3, 6]
    nums = [5, 1, None, None, 4, 3, None, None, 6, None, None]
    nums = [2, 1, None, None, 3, None, None]
    nums = []
    nums = [10, 5, None, None, 15, 6, None, None, 20, None, None]
    root = build_tree(nums)
    print_tree(root)
    print(isValidBST(root))

