# -*- coding: utf-8 -*-
# @Time        : 2019/7/19 10:35
# @Author      : tianyunzqs
# @Description : 

"""
92. Reverse Linked List II
Medium

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
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


def reverse(head, other_head):
    if not head:
        return other_head

    cur = head
    while cur.next:
        tmp = cur.next
        cur.next = tmp.next
        tmp.next = head
        head = tmp

    cur.next = other_head
    return head


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    # 保存小于m的节点
    dummy1 = p1 = ListNode(-1)
    # 保存m~n之间的节点（需要翻转的节点）
    dummy2 = p2 = ListNode(-1)
    # 保存大于n的节点
    dummy3 = p3 = ListNode(-1)
    cur = head
    cnt = 0
    while cur:
        cnt += 1
        if cnt < m:
            p1.next = cur
            p1 = p1.next
        elif m <= cnt <= n:
            p2.next = cur
            p2 = p2.next
        else:
            p3.next = cur
            p3 = p3.next
        cur = cur.next

    p2.next = None
    p3.next = None
    reverse_p2 = reverse(dummy2.next, dummy3.next)
    p1.next = reverse_p2

    return dummy1.next


if __name__ == '__main__':
    a = [1, 2]
    # a = [1, 1, 1, 4, 5]
    # a = [1,1,2,3,3]
    # a = [1, 2, 3, 4, 5]
    head = build_linklist(a)
    print_linklist(head)
    new_head = reverseBetween(head, 1, 2)
    print_linklist(new_head)
