# -*- coding: utf-8 -*-
# @Time        : 2019/6/11 13:43
# @Author      : tianyunzqs
# @Description : 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            self.next.next = self.next
            return self.__str__()
        else:
            _str = str(self.val) if self.val else ''
            return _str


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    list_len = 1
    p = head
    while p.next:
        list_len += 1
        p = p.next

    if n == list_len:
        return head.next

    cnt = 1
    while head.next:
        cnt += 1
        if cnt == list_len - n:
            head.next = head.next.next


a = ListNode(1)
a.next = ListNode(2)
print(a)
# p = a
# for i in range(2, 5):
#     t = ListNode(i)
#     p.next = t




