# -*- coding: utf-8 -*-
# @Time        : 2019/7/15 10:07
# @Author      : tianyunzqs
# @Description : 


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


def reverse_linklist(head: ListNode):
    if not head:
        return head

    cur = head
    while cur.next:
        p = cur.next
        cur.next = p.next
        p.next = head
        head = p

    return head


if __name__ == '__main__':
    a = []
    head = build_linklist(a)
    print_linklist(head)
    new_head = reverse_linklist(head)
    print_linklist(new_head)
