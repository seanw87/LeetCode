# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            cur = head  # 记录cur初始引用（位置）
            head = head.next
            cur.next = prev  # 此处head的地址已改变（重新赋值引用），因此不能写为head.next=prev；
            # 这行也不能放置于head=head.next之前，因为cur.next改变意味着head.next改变
            # 此时修改cur.next的值并不会影响head，因为head已被重新赋值（改变地址）
            prev = cur

            # 或更简洁的写法：
            # cur.next, cur, prev = prev, cur.next, cur

        return prev


ln = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, None))))
res = Solution1.reverseList(ln)
while res:
    print(res.val)
    res = res.next


class Solution2:
    """
    recursion (same logic)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        cur = node
        node = node.next
        cur.next = prev
        return self._reverse(node, cur)


class Solution3:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, head, prev = prev, head.next, head
        return prev


print()
ln = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, None))))
res = Solution3.reverseList(ln)
while res:
    print(res.val)
    res = res.next
