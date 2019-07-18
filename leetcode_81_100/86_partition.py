# -*- coding: utf-8 -*-
# @Time        : 2019/7/18 12:38
# @Author      : tianyunzqs
# @Description : 

"""
86. Partition List
Medium

Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
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


def partition(head: ListNode, x: int) -> ListNode:
    # 小于x的单链表
    dummy1 = p1 = ListNode(-1)
    # 大于x的单链表
    dummy2 = p2 = ListNode(-1)
    cur = head
    while cur:
        if cur.val < x:
            p1.next = cur
            p1 = p1.next
        else:
            p2.next = cur
            p2 = p2.next

        cur = cur.next

    # 截断大于x的单链表
    p2.next = None
    # 将小于x的单链表尾与大于x的单链表头连接起来
    p1.next = dummy2.next

    return dummy1.next


if __name__ == '__main__':
    a = [1, 4, 3, 2, 5, 2]
    a = [4, 1]
    head = build_linklist(a)
    print_linklist(head)
    new_head = partition(head, 3)
    print_linklist(new_head)
