# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        even = head.next
        eh = even  # store the starter point of even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = eh
        return head
