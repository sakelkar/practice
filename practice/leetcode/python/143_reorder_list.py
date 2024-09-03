from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reorderList(self, head: Optional[ListNode]):
        if not head: return None

        slow, fast = head, head.next
        while fast and fast.next:
            if slow:
                slow = slow.next
            if fast:
                fast = fast.next.next

        if slow and slow.next:
            p2 = self.reverseList(slow.next)

        if slow:
            slow.next = None

        dummyNode = ListNode(-1)
        p1, curr = head, dummyNode
        cnt = 0

        while p1 or p2:
            if p1 and curr and cnt % 2 == 0:
                curr.next = p1
                p1 = p1.next
            elif curr and p2:
                curr.next = p2
                p2 = p2.next

            cnt += 1
            if curr:
                curr = curr.next

        return dummyNode.next
