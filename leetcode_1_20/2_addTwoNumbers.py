# -*- coding: utf-8 -*-
# @Time        : 2019/7/5 15:45
# @Author      : tianyunzqs
# @Description : 

"""
2. Add Two Numbers
Medium


You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def print_linklist(head: ListNode):
    val_list = []
    while head:
        val_list.append(str(head.val))
        head = head.next

    print('->'.join(val_list))


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    解题思路：链表加法.
    题中已说明给定的两个链表已作倒序排列，故只需定义一个carry，其值等于两链表对应位置的和与前一位置的余数之和
    最后将carry对10取整（如果相加超过10，则最后输出链表多一个节点，该节点为进位数），建立输出链表。
    :param l1:
    :param l2:
    :return:
    """
    dummy = p = ListNode(-1)
    a, b, carry = 0, 0, 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        p.next = ListNode(carry % 10)
        p = p.next
        carry //= 10
    return dummy.next


if __name__ == '__main__':
    a = [9, 3, 5]
    b = [1, 6, 4]
    aa = build_linklist(a)
    bb = build_linklist(b)
    c = addTwoNumbers(aa, bb)
    print_linklist(c)
