# -*- coding: utf-8 -*-
# @Time        : 2021/4/29 14:42
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
109. 有序链表转换二叉搜索树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


import uuid
from random import sample
from typing import List
from graphviz import Digraph


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_linklist(val_list: list) -> ListNode:
    if not val_list:
        return None

    head = ListNode(val_list[0])
    tp = head
    for val in val_list[1:]:
        newNode = ListNode(val)
        tp.next = newNode
        tp = newNode

    return head


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
    def list2array(self, head: ListNode):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        # 将列表从中间切开，小的部分是左子树，大的部分是右子树
        mid_idx = len(nums) // 2
        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx+1:])
        return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = self.list2array(head)
        if not nums:
            return None
        # 将列表从中间切开，小的部分是左子树，大的部分是右子树
        mid_idx = len(nums) // 2
        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx+1:])
        return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    list_head = build_linklist(nums)
    tree_root = Solution().sortedListToBST(list_head)
    print(print_tree_preorder(tree_root))
