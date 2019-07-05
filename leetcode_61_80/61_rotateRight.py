# -*- coding: utf-8 -*-
# @Time        : 2019/7/2 8:48
# @Author      : tianyunzqs
# @Description : 


"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
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


def rotateRight(head: ListNode, k: int) -> ListNode:
    if k == 0 or not head or not head.next:
        return head

    def fun(head, k):
        if k > 1:
            pre_a = None
            a = head
            b = head
            while a.next:
                pre_a = a
                a = a.next
            pre_a.next = None
            a.next = b
            a = fun(a, k-1)
            return a
        return head

    tmp = head
    link_len = 0
    while tmp:
        link_len += 1
        tmp = tmp.next
    k = k % link_len
    return fun(head, k)


if __name__ == '__main__':
    y = [1, 2]
    head = build_linklist(y)
    print_linklist(head)
    a = rotateRight(head, 2)
    print_linklist(a)
