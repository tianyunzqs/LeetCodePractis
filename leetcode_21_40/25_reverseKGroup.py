# -*- coding: utf-8 -*-
# @Time        : 2019/6/14 9:30
# @Author      : tianyunzqs
# @Description : 

"""
25. Reverse Nodes in k-Group
Hard


Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
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


def reverseKGroup(head, k):

    # base case, look k steps forward to see if the block needs to be reversed
    # if the length is less than k, do nothing, return the current head
    nextHead = head
    for i in range(0, k):
        if not nextHead:
            return head
        nextHead = nextHead.next

    # the length is greater than k, reverse the first k
    prev = None
    connect = cur = head
    for i in range(0, k):
        # cur.next = prev
        # cur = cur.next
        # prev = cur
        cur.next, cur, prev = prev, cur.next, cur

    # recursively call on rest of the list then connect two parts
    connect.next = reverseKGroup(nextHead, k)

    return prev


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    head = build_linklist(a)
    # print_linklist(head)
    new_head = reverseKGroup(head, 3)
    print_linklist(new_head)

