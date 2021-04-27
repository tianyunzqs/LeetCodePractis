# -*- coding: utf-8 -*-
# @Time        : 2021/4/23 14:17
# @Author      : tianyunzqs
# @Description :

"""
https://leetcode-cn.com/problems/recover-binary-search-tree/
99. 恢复二叉搜索树
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

示例 1：
输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

示例 2：
输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。

提示：
树上节点的数目在范围 [2, 1000] 内
-2^31 <= Node.val <= 2^31 - 1
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
        bt.left = build_tree(nums)
        bt.right = build_tree(nums)

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
    def print_tree_inorder(self, root: TreeNode):
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

        inoder(root)
        return res

    def recoverTree2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 中序遍历得到错误的位置下标
        inoder_list = self.print_tree_inorder(root)
        res = []
        for i in range(len(inoder_list)-1):
            if inoder_list[i] > inoder_list[i+1]:
                res.append((i, i+1))

        # 题目中限定了两个节点错误，因此只存在一组下表或2组下标
        if not res:
            return
        elif len(res) == 1:  # 1组下标
            id1, id2 = res[0]
        elif len(res) == 2:  # 2组下标
            id1 = res[0][0]
            id2 = res[1][1]
        else:
            return

        self.id1_node, self.id2_node = None, None
        self.cnt = 0

        def inoder(root):
            if root:
                inoder(root.left)
                # 再次中序遍历，根据下标确定交换的两个节点
                if self.cnt == id1:
                    self.id1_node = root
                if self.cnt == id2:
                    self.id2_node = root
                self.cnt += 1
                inoder(root.right)

        inoder(root)
        # 交换两个节点的值
        self.id1_node.val, self.id2_node.val = self.id2_node.val, self.id1_node.val

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first_node = None
        self.second_node = None
        self.pre_node = TreeNode(float("-inf"))

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if self.first_node is None and self.pre_node.val >= root.val:
                self.first_node = self.pre_node
            if self.first_node and self.pre_node.val >= root.val:
                self.second_node = root
            self.pre_node = root
            in_order(root.right)

        in_order(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val


if __name__ == '__main__':
    # nums = [5, 1, None, None, 4, 3, None, None, 6, None, None]
    # tree_root = build_tree(nums)
    # print(print_tree_preorder(tree_root))
    # view_tree(tree_root)

    # nums = ['A', 'B', 'D', 'H', 'P', None, None, 'Q', None, None, 'I', 'R', None, None, 'S', None, None,
    #         'E', 'J', 'T', None, None, 'U', None, None, 'K', 'V', None, None, 'W', None, None, 'C', 'F', 'L',
    #         'X', None, None, 'Y', None, None, 'M', None, 'Z', None, None, 'G', 'N', None, None, 'O', None, None]
    # tree_root = build_tree(nums)
    # print(print_tree_preorder(tree_root))
    # view_tree(tree_root)

    # nums = [1, 3, None, 2, None, None, None]
    # tree_root = build_tree(nums)
    # print(print_tree_inorder(tree_root))
    # Solution().recoverTree(tree_root)
    # print(print_tree_inorder(tree_root))

    nums = [3, 1, None, None, 4, 2, None, None, None]
    tree_root = build_tree(nums)
    print(print_tree_inorder(tree_root))
    Solution().recoverTree(tree_root)
    print(print_tree_inorder(tree_root))

    # nums = [3, 8, 1, None, None, None, 4, None, 2, None, None]
    # tree_root = build_tree(nums)
    # print(print_tree_inorder(tree_root))
    # Solution().recoverTree2(tree_root)
    # print(print_tree_inorder(tree_root))
