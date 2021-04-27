# -*- coding: utf-8 -*-
# @Time        : 2021/4/27 19:26
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/symmetric-tree/
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

进阶：
你可以运用递归和迭代两种方法解决这个问题吗？
"""


from graphviz import Digraph
import uuid
from random import sample


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
    def fun(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.fun(p.left, q.right) and self.fun(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif (not root.left and root.right) or (root.left and not root.right):
            return False
        else:
            return self.fun(root.left, root.right)


if __name__ == '__main__':
    nums = [3, 1, None, None, 4, 2, None, None, None]
    nums = [1, 2, 3, None, None, 4, None, None, 2, 4, None, None, 3, None, None]
    nums = [1, 2, None, 3, None, None, 2, None, 3, None, None]
    nums = [1, None, None]
    tree_root = build_tree(nums, [0])
    # view_tree(tree_root)
    print(print_tree_preorder(tree_root))
    print(Solution().isSymmetric(tree_root))
