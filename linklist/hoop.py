# -*- coding: utf-8 -*-
# @Time        : 2019/7/15 10:24
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


def build_hoop_linklist(val_list: list) -> ListNode:
    if not val_list:
        return None

    head = ListNode(val_list[0])
    tp = head
    for val in val_list[1:]:
        newNode = ListNode(val)
        tp.next = newNode
        tp = newNode

    tp.next = head

    return head


def print_linklist(head: ListNode):
    val_list = []
    while head:
        val_list.append(str(head.val))
        head = head.next

    print('->'.join(val_list))


def hoop_linklist(head: ListNode):
    p1, p2 = head, head
    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False


def hoop_linklist2(head: ListNode):
    p1, p2 = head, head
    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            p2 = head
            while True:
                if p1 == p2:
                    return p1
                p1 = p1.next
                p2 = p2.next

    return None


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    head = build_hoop_linklist(a)
    print(hoop_linklist(head))
    print(hoop_linklist2(head))
