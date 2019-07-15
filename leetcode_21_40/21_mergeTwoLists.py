# -*- coding: utf-8 -*-
# @Time        : 2019/7/6 17:59
# @Author      : tianyunzqs
# @Description ：

"""
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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


def traverse(head: ListNode) -> list:
    current = head
    nums = []
    while current:
        nums.append(current.val)
        current = current.next

    return nums


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    nums1 = traverse(l1)
    nums2 = traverse(l2)

    allNumbers = sorted(nums1 + nums2)

    if not allNumbers:
        return None

    return build_linklist(allNumbers)


def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
    """
     递归解法
     递归的核心方法是将问题规模不断缩小化
     合并两个长度为n和m的链表，在value(n) < value(m)可以将规模缩减为合并长度为(n-1)和m的链表
    """
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = mergeTwoLists2(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists2(l1, l2.next)
        return l2


def mergeTwoLists3(l1: ListNode, l2: ListNode) -> ListNode:
    """
     遍历解法(有错误)
     同时不断遍历两个链表，取出小的追加到新的头节点后，直至两者其中一个为空
     再将另一者追加的新链表最后
    """
    dummy = ListNode(-1)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 if l1 else l2

    return dummy.next


if __name__ == '__main__':
    a = [1, 2, 4]
    b = [1, 3, 4]
    l1 = build_linklist(a)
    l2 = build_linklist(b)
    print_linklist(l1)
    print_linklist(l2)

    new_head2 = mergeTwoLists2(l1, l2)
    new_head3 = mergeTwoLists3(l1, l2)
    print_linklist(new_head2)
    print_linklist(new_head3)
