# -*- coding: utf-8 -*-
# @Time        : 2019/6/14 9:30
# @Author      : tianyunzqs
# @Description : 

"""
24. Swap Nodes in Pairs
Medium


Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.


Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
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


def swap_list_node(head: ListNode, pos1: int, pos2: int) -> ListNode:
    if not head or not head.next or pos1 == pos2:
        return head

    pos = 0
    cur_tp = head
    while cur_tp.next:
        if pos == pos1:
            pass
        pos += 1


# 24. Swap Nodes in Pairs
def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    pre_tp = head
    cur_tp = head.next
    new_head = cur_tp
    while cur_tp:
        tmp = pre_tp
        pre_tp.next = cur_tp.next
        cur_tp.next = pre_tp
        if pre_tp.next and pre_tp.next.next:
            pre_tp = pre_tp.next
            cur_tp = pre_tp.next
            tmp.next = cur_tp
        else:
            break
    return new_head


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    head = build_linklist(a)
    # print_linklist(head)
    new_head = swapPairs(head)
    print_linklist(new_head)

