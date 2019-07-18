# -*- coding: utf-8 -*-
# @Time        : 2019/7/17 18:07
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


def deleteDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    pre = head
    cur = head.next
    dummy2 = dummy = ListNode(-1)
    while cur:
        # 如果前后节点值不同，则保存前一个节点
        if pre.val != cur.val:
            dummy.next = pre
            dummy = dummy.next
        pre = cur
        cur = cur.next

    # 因为cur是后一个节点，因此需要加上前一个节点
    dummy.next = pre

    return dummy2.next


if __name__ == '__main__':
    a = [1, 2, 3, 3, 4, 4, 5]
    # a = [1, 1, 1, 4, 5]
    # a = [1,1,2,3,3]
    # a = [1, 2, 3, 3]
    head = build_linklist(a)
    print_linklist(head)
    new_head = deleteDuplicates(head)
    print_linklist(new_head)
