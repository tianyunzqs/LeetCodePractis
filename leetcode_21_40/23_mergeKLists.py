# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 18:19
# @Author      : tianyunzqs
# @Description ：

"""
23. Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def link2list(head: ListNode) -> list:
    val_list = []
    while head:
        val_list.append(head.val)
        head = head.next
    return val_list


def buildLink(val_list: list) -> ListNode:
    if not val_list:
        return None

    head = ListNode(val_list[0])
    tp = head
    for val in val_list[1:]:
        newNode = ListNode(val)
        tp.next = newNode
        tp = newNode

    return head


def mergeKLists(lists) -> ListNode:
    vals = []
    for _list in lists:
        vals += link2list(_list)
    vals = sorted(vals)
    head = buildLink(vals)

    return head
