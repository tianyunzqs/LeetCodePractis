# -*- coding: utf-8 -*-
# @Time        : 2019/7/17 17:14
# @Author      : tianyunzqs
# @Description : 

"""
82. Remove Duplicates from Sorted List II
Medium

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
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


def deleteDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    dummy2 = dummy = ListNode(-1)
    pre = None
    cur = head
    while cur.next:
        aft = cur.next
        if pre:
            # 如果当前节点值与前后节点值都不同，则需要保存
            if pre.val != cur.val and cur.val != aft.val:
                dummy.next = cur
                dummy = dummy.next  # 节点前进一位，保存值，如果不加这句，则不会保存已保存过的值
        else:
            # 如果没有前置节点，而且当前节点与后置节点不同，则保存
            if cur.val != aft.val:
                dummy.next = cur
                dummy = dummy.next
        pre = cur
        cur = cur.next

    if cur.val != pre.val:
        dummy.next = cur
        dummy = dummy.next

    dummy.next = None
    return dummy2.next


if __name__ == '__main__':
    a = [1, 2, 3, 3, 4, 4, 5]
    a = [1, 1, 1, 4, 5]
    head = build_linklist(a)
    print_linklist(head)
    new_head = deleteDuplicates(head)
    print_linklist(new_head)
