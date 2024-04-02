# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    not smart way (with two loops)
    """

    @staticmethod
    def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
        ll = head
        ln = 1
        while ll.next:
            ln += 1
            ll = ll.next
        if ln == 1:  # 需要判断仅有一个元素的情况
            return None

        middle = math.floor(ln / 2)
        ll = head  # python中对象赋值其实是对象引用(object reference)
        for i in range(middle - 1):
            ll = ll.next
        ll.next = ll.next.next
        return head


class Solution2:
    """
    slow-fast pointer
    """

    @staticmethod
    def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        fast_pointer = head.next.next  # control the pointer location
        slow_pointer = head
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        slow_pointer.next = slow_pointer.next.next
        return head
