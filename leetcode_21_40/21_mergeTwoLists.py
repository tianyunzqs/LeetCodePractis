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


def buildList(numbers: list) -> ListNode:
    head = ListNode(numbers[0])
    current = head
    for num in numbers[1:]:
        newNode = ListNode(num)
        current.next = newNode
        current = newNode

    return head


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

    return buildList(allNumbers)



