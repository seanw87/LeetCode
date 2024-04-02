# Definition for singly-linked list.
import copy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    wrong solution: parameter passing is also by reference, which changed the head structure.
    Can only use deepcopy, which is very low-efficient
    """

    def pairSum(self, head: Optional[ListNode]) -> int:
        maxv = 0
        rev_head, n = self._revListNode(copy.deepcopy(head))
        for i in range(int(n / 2)):
            sumval = head.val + rev_head.val
            maxv = max(maxv, sumval)
            head = head.next
            rev_head = rev_head.next
        return maxv

    def _revListNode(self, head):
        prev = None
        n = 0
        while head:
            head.next, head, prev = prev, head.next, head
            n += 1
        return prev, n


ln = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, None))))
print(Solution1().pairSum(ln))


class Solution2:
    """
    fast-slow pointer to locate at the middle, then reverse the right
    Not efficient
    """

    def pairSum(self, head: Optional[ListNode]) -> int:
        fp = head.next
        sp = head
        prev = None
        resmax = 0
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        # reverse the rest LinkedList
        while sp:
            cur = sp
            sp = sp.next
            cur.next = prev
            prev = cur

        while head and prev:
            res = head.val + prev.val
            print(head.val, prev.val, res)
            resmax = max(res, resmax)
            head = head.next
            prev = prev.next
        return resmax


ln = ListNode(1,
              next=ListNode(2,
                            next=ListNode(3,
                                          next=ListNode(4, ListNode(5,
                                                                    next=ListNode(6, None))))))
print(Solution2().pairSum(ln))


class Solution3:
    """
    fast-slow pointer to locate at the middle, when looping, reverse the left
    high efficient
    """

    @staticmethod
    def pairSum(head: Optional[ListNode]) -> int:
        fp = head
        sp = head
        prev = None
        resmax = 0
        while fp and fp.next:
            fp = fp.next.next
            cur = sp
            sp = sp.next
            cur.next = prev
            prev = cur
        while sp:
            res = sp.val + prev.val
            print(sp.val, prev.val, res)
            resmax = max(res, resmax)
            sp = sp.next
            prev = prev.next

        return resmax


ln = ListNode(1,
              next=ListNode(2,
                            next=ListNode(3,
                                          next=ListNode(4, ListNode(5,
                                                                    next=ListNode(6, None))))))
print("solution3")
print(Solution3.pairSum(ln))
